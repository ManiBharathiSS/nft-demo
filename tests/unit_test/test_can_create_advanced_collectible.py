from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_contract
import pytest
from brownie import network
from scripts.Advanced_collectible.deploy_and_create import deploy_and_create


def test_can_create_advanced_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    advanced_collectible, creation_transaction = deploy_and_create()
    request_id = creation_transaction.events["requestedCollectible"]["requestID"]
    random_number = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        request_id, random_number, advanced_collectible.address
    )
    assert advanced_collectible.tokenCounter() == 1
    assert advanced_collectible.tokedIdToBreed(1) == random_number % 3
