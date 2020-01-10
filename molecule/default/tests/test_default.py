import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_config_file(host):
    f = host.file('/opt/services/vault/config.hcl')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_vault_service_available(host):
    cmd = host.run("curl -LI 172.17.0.2:8200/ui/ -o /dev/null -w '%{http_code}\n' -s")  # noqa

    assert cmd.stdout == '200\n'
