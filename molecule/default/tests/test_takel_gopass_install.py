import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_gopass_install_deb_packages_installed(host, testvars):
    install_packages = testvars['takel_gopass_deb_install_packages']

    for install_package in install_packages:
        package = host.package(install_package)

        assert package.is_installed


def test_takel_gopass_install_deb_package_removed(host, testvars):
    deb = testvars['takel_gopass_tmp']

    assert not host.file(deb).exists


def test_takel_gopass_install_template_pass(host):
    file = host.file('/usr/local/bin/pass')

    assert file.exists
    assert file.is_file
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == 0o755
