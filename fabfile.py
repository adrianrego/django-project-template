from fabric.api import env, run, sudo, local
from fabric import network


def vagrant():
    # change from the default user to 'vagrant'
    env.user = 'vagrant'
    # connect to the port-forwarded ssh
    env.hosts = ['127.0.0.1:2222']

    # use vagrant ssh key
    result = local("vagrant ssh_config | grep IdentityFile", capture=True)
    env.key_filename = result.split()[1]


def upgrade_packages():
    sudo("apt-get update")
    sudo("apt-get upgrade -y")


def bootstrap():
    # Upgrade system packages
    upgrade_packages()

    # Install basic package requirements
    sudo("apt-get install -y build-essential git-core subversion mercurial "
                            "bison openssl libreadline6 libreadline6-dev "
                            "curl zlib1g zlib1g-dev libssl-dev libyaml-dev "
                            "libsqlite3-0 libsqlite3-dev sqlite3 libxml2-dev "
                            "libxslt-dev autoconf libc6-dev ncurses-dev "
                            "python-dev python-software-properties")

    # Add Postgresql and Nginx PPAs
    sudo("add-apt-repository ppa:pitti/postgresql")
    sudo("add-apt-repository ppa:nginx/stable")
    sudo("apt-get update")

    # System-Wide RVM install
    sudo("bash < <(curl -sk https://rvm.beginrescueend.com/install/rvm)")
    sudo("usermod -a -G rvm %s" % env.user)

    # Disconnect to have RVM properly load
    network.disconnect_all()

    # Install Ruby and Chef
    rvm_install('ruby-1.9.2-p290', True)
    run("gem install chef ohai --no-ri --no-rdoc")


def rvm_install(ruby, default=False):
    run("rvm install %s" % ruby)

    if default:
        run("rvm use %s --default" % ruby)
