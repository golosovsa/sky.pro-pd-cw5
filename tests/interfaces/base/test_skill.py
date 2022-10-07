"""
    Test base Skill
"""


class TestSkill:

    def test_constructor(self, derived_skill):
        derived = derived_skill()
        private = derived_skill("Private", 20.0, 20.0)

        assert derived.name != private.name
        assert derived.stamina != private.stamina
        assert derived.damage != private.damage

        assert derived.name == "Derived"
        assert private.name == "Private"

    def test_skill_effect(self, derived_skill_instance, derived_unit_instance_1, derived_unit_instance_2):
        message = derived_skill_instance.skill_effect(
            derived_unit_instance_1,
            derived_unit_instance_2
        )
        assert derived_unit_instance_1.name in message
        assert derived_unit_instance_2.name in message
        assert derived_skill_instance.name in message
        assert str(None) not in message

    def test_use(self, derived_skill_instance, derived_unit_instance_1, derived_unit_instance_2):
        message = derived_skill_instance.use(
            derived_unit_instance_1,
            derived_unit_instance_2
        )
        assert derived_unit_instance_1.name in message
        assert derived_unit_instance_2.name in message
        assert derived_skill_instance.name in message
        assert str(None) not in message

    def test_use_not_enough_stamina(self, derived_skill_instance,
                                    derived_unit_instance_1, derived_unit_instance_low_stamina):
        message = derived_skill_instance.use(
            derived_unit_instance_low_stamina,
            derived_unit_instance_1,
        )

        assert derived_unit_instance_1.name not in message
        assert derived_unit_instance_low_stamina.name in message
        assert derived_skill_instance.name in message
        assert str(None) not in message
