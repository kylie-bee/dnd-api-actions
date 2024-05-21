"""
A module that contains the actions that can be performed on the D&D 5e API.

"""

import dnd5epy
from dnd5epy.rest import ApiException
from sema4ai.actions import action

# Defining the host is optional and defaults to https://www.dnd5eapi.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dnd5epy.Configuration(host="https://www.dnd5eapi.co")
ABILITY_SCORE_NAMES = ["str", "dex", "con", "int", "wis", "cha"]


@action
def get_ability_score_models() -> dict[str, dict]:
    """
    Get all ability scores from the API.

    These4 scores represent one of the six abilities that describes a creature's
    physical and mental characteristics. The three main rolls of the game - the
    ability check, the saving throw, and the attack roll - rely on the ability scores.

    Returns:
        ability_score_descriptions: A dictionary with the ability score names as keys
            and the ability score models as values.

            Example:

            {
                "str": {
                    "index": "str",
                    "name": "Strength",
                    "full_name": "Strength",
                    "desc": [
                        "Strength measures bodily power, athletic training, and the extent to which you can exert raw physical force."
                    ],
                    "skills": [
                        {
                            "name": "Athletics",
                            "url": "/api/skills/athletics"
                        }
                    ],
                    "url": "/api/ability-scores/str"
                },
                "dex": {
                    "index": "dex",
                    "name": "Dexterity",
                    "full_name": "Dexterity",
                    "desc": [
                        "Dexterity measures agility, reflexes, and balance."
                    ],
                    "skills": [
                        {
                            "name": "Acrobatics",
                            "url": "/api/skills/acrobatics"
                        },
                        {
                            "name": "Sleight of Hand",
                            "url": "/api/skills/sleight-of-hand"
                        },
                        {
                            "name": "Stealth",
                            "url": "/api/skills/stealth"
                        }
                    ],
                    "url": "/api/ability-scores/dex"
                },
                "con": {
                    "index": "con",
                    "name": "Constitution",
                    "full_name": "Constitution",
                    "desc": [
                        "Constitution measures health, stamina, and vital force."
                    ],
                    "url": "/api/ability-scores/con"
                },
                "int": {
                    "index": "int",
                    "name": "Intelligence",
                    "full_name": "Intelligence",
                    "desc": [
                        "Intelligence measures mental acuity, accuracy of recall, and the ability to reason."
                    ],
                    "skills": [
                        {
                            "name": "Arcana",
                            "url": "/api/skills/arcana"
                        },
                        {
                            "name": "History",
                            "url": "/api/skills/history"
                        },
                        {
                            "name": "Investigation",
                            "url": "/api/skills/investigation"
                        },
                        {
                            "name": "Nature",
                            "url": "/api/skills/nature"
                        },
                        {
                            "name": "Religion",
                            "url": "/api/skills/religion"
                        }
                    ],
                    "url": "/api/ability
    """
    ability_score_descriptions = {}
    # Enter a context with an instance of the API client
    with dnd5epy.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = dnd5epy.CharacterDataApi(api_client)

        try:
            # Get all ability scores.
            for name in ABILITY_SCORE_NAMES:
                api_response = api_instance.api_ability_scores_index_get(name)
                ability_score_descriptions[name] = api_response.to_dict()
        except ApiException as e:
            print(
                "Exception when calling CharacterDataApi->api_ability_scores_get: %s\n"
                % e
            )

    return ability_score_descriptions


@action
def get_background_models() -> dict[str, dict]:
    """
    Get all backgrounds from the API.

    Backgrounds provide a way to create a character with a rich and interesting
    backstory. They can be used to help flesh out a character's personality and
    provide some additional roleplaying opportunities.

    Returns:
        background_descriptions: A dictionary with the background names as keys
            and the background models as values.

            Example:

            {
                "acolyte": {
                    "index": "acolyte",
                    "name": "Acolyte",
                    "url": "/api/backgrounds/acolyte",
                    "skill_proficiencies": [
                        {
                            "name": "Insight",
                            "url": "/api/skills/insight"
                        },
                        {
                            "name": "Religion",
                            "url": "/api/skills/religion"
                        }
                    ],
                    "tool_proficiencies": [
                        {
                            "name": "None",
                            "url": ""
                        }
                    ],
                    "languages": [
                        {
                            "name": "Two of your choice",
                            "url": ""
                        }
                    ],
                    "equipment": [
                        {
                            "item": {
                                "name": "Holy Symbol",
                                "url": "/api/equipment/holy-symbol"
                            },
                            "quantity": 1
                        },
                        {
                            "item": {
                                "name": "Prayer Book",
                                "url": "/api/equipment/prayer-book"
                            },
                            "quantity": 1
                        },
                        {
                            "item": {
                                "name": "Vestments",
                                "url": "/api/equipment/vestments"
                            },
                            "quantity": 1
                        },
                        {
                            "item": {
                                "name": "Set of Common Clothes",
                                "url": "/api/equipment/clothes-common"
                            },
                            "quantity": 1
                        },
                        {
                            "item": {
                                "name": "Belt Pouch",
                                "url": "/api/equipment/belt-pouch"
                            },
                            "quantity": 1
                        },
                        {
                            "item": {
                                "name": "5 gp",
                                "url": ""
                            },
                            "quantity": 1
                        }
                    ],
                    ...
                },
                ...
            }

    """
    background_descriptions = {}
    # Enter a context with an instance of the API client
    with dnd5epy.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = dnd5epy.CharacterDataApi(api_client)

        try:
            # Get all backgrounds.
            # TODO: THIS WILL FAIL
            api_response = api_instance.api_backgrounds_get_not_real_method()
            for background in api_response.results:
                background_name = background.index
                background_descriptions[background_name] = background.to_dict()
        except ApiException as e:
            print(
                "Exception when calling CharacterDataApi->api_backgrounds_get: %s\n" % e
            )

    return background_descriptions
