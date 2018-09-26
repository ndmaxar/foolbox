import numpy as np

from foolbox.attacks import CarliniWagnerAttack as Attack


def test_targeted_attack(bn_targeted_adversarial):
    adv = bn_targeted_adversarial
    attack = Attack()
    attack(adv)
    assert adv.image is not None
    assert adv.distance.value < np.inf


def test_attack_impossible(bn_impossible):
    adv = bn_impossible
    attack = Attack()
    attack(adv)
    assert adv.image is None
    assert adv.distance.value == np.inf
