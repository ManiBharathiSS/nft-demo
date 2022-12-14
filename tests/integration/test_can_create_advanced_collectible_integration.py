from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_contract
import pytest
from brownie import network
from scripts.Advanced_collectible.deploy_and_create import deploy_and_create
import time


def test_can_create_advanced_collectible_integration():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    advanced_collectible, creation_transaction = deploy_and_create()
    time.sleep(240)
    assert advanced_collectible.tokenCounter() == 1
