from framework.tools.functions import get_command_arguments
from .globals import FUT_MAIN_GLOBAL
from .globals import ExpectedShellResult
import pytest


@pytest.mark.dependency(name="brv_fut_setup_dut", depends=["dut_ready"], scope='session')
def test_brv_fut_setup_dut():
    dut_handler = pytest.dut_handler
    assert dut_handler.transfer(manager='dm')
    assert dut_handler.run('tests/dm/brv_setup') == ExpectedShellResult


# Read entire testcase configuration
brv_config = FUT_MAIN_GLOBAL.get_test_config(cfg_file_prefix='BRV')


########################################################################################################################
brv_ovs_correct_version_args = brv_config.get('brv_ovs_correct_version', [])


@pytest.mark.dut_only()
@pytest.mark.parametrize('test_config', brv_ovs_correct_version_args)
@pytest.mark.dependency(depends=["brv_fut_setup_dut"], scope='session')
def test_brv_ovs_correct_version(test_config):
    dut_handler = pytest.dut_handler
    test_args = get_command_arguments(test_config['ovs_ver'])
    assert dut_handler.run('tests/dm/brv_ovs_correct_version', test_args) == ExpectedShellResult


########################################################################################################################
brv_is_script_on_system_fut_args = brv_config.get('brv_is_script_on_system_fut', [])


@pytest.mark.dut_only()
@pytest.mark.parametrize('test_config', brv_is_script_on_system_fut_args)
@pytest.mark.dependency(depends=["brv_fut_setup_dut"], scope='session')
def test_brv_is_script_on_system_fut(test_config):
    dut_handler = pytest.dut_handler
    test_args = get_command_arguments(test_config['script'])
    assert dut_handler.run('tests/dm/brv_is_script_on_system', test_args) == ExpectedShellResult


########################################################################################################################
brv_is_tool_on_system_fut_args = brv_config.get('brv_is_tool_on_system_fut', [])


@pytest.mark.dut_only()
@pytest.mark.parametrize('test_config', brv_is_tool_on_system_fut_args)
@pytest.mark.dependency(depends=["brv_fut_setup_dut"], scope='session')
def test_brv_is_tool_on_system_fut(test_config):
    dut_handler = pytest.dut_handler
    test_args = get_command_arguments(test_config['tool'])
    assert dut_handler.run('tests/dm/brv_is_tool_on_system', test_args) == ExpectedShellResult


########################################################################################################################
brv_is_tool_on_system_opensync_args = brv_config.get('brv_is_tool_on_system_opensync', [])


@pytest.mark.dut_only()
@pytest.mark.parametrize('test_config', brv_is_tool_on_system_opensync_args)
@pytest.mark.dependency(depends=["brv_fut_setup_dut"], scope='session')
def test_brv_is_tool_on_system_opensync(test_config):
    dut_handler = pytest.dut_handler
    test_args = get_command_arguments(test_config['tool'])
    assert dut_handler.run('tests/dm/brv_is_tool_on_system', test_args) == ExpectedShellResult


########################################################################################################################
brv_busybox_builtins_args = brv_config.get('brv_busybox_builtins', [])


@pytest.mark.dut_only()
@pytest.mark.parametrize('test_config', brv_busybox_builtins_args)
@pytest.mark.dependency(depends=["brv_fut_setup_dut"], scope='session')
def test_brv_busybox_builtins(test_config):
    dut_handler = pytest.dut_handler
    test_args = get_command_arguments(test_config['tool'])
    assert dut_handler.run('tests/dm/brv_busybox_builtins', test_args) == ExpectedShellResult


########################################################################################################################
