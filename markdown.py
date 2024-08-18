from npc import Npc


def build_stat_block(npc: Npc):
    abilities = build_abilities(npc)
    actions = build_actions(npc)
    legendary_actions = build_legendary_actions(npc)
    bonus_actions = build_bonus_actions(npc)
    page = f"""
## {npc.name}
*{npc.creature_type}*
___
**Armor Class** :: {npc.armor_class}
**Hit Points**  :: {npc.hitpoints}
**Speed**       :: {npc.movement_speed}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|{npc.abilities.strength}|{npc.abilities.dexterity}|{npc.abilities.constitution}|{npc.abilities.intelligence}|{npc.abilities.wisdom}|{npc.abilities.charisma}|
___
**Condition Immunities** :: {npc.condition_immunities}
**Senses**               :: {npc.senses}
**Languages**            :: {npc.languages}
**Challenge**            :: {npc.challenge_rating}
___
{abilities}
### Actions
{actions}
{bonus_actions}
{legendary_actions}

"""

    with open("monster.txt", "w") as f:
        f.write("{{monster,frame")
        f.write(page)
        f.write("}}")


def build_actions(npc: Npc):
    actions = ""
    if not npc.actions:
        return actions
    for action in npc.actions:

        action = f"***{action.name}*** {action.effect}\n:\n"
        actions = actions + action
    return actions

def build_abilities(npc: Npc):
    abilities = ""
    if not npc.special_abilities:
        return abilities
    for special_ability in npc.special_abilities:

        ability = f"***{special_ability.name}*** {special_ability.effect}\n:\n"
        abilities = abilities + ability
    return abilities


def build_bonus_actions(npc: Npc):

    if npc.bonus_actions:
        actions = "### Bonus Actions\n"
        for action in npc.bonus_actions:

            action = f"***{action.name}*** {action.effect}\n:\n"
            actions = actions + action
        return actions
    else:
        return ""


def build_legendary_actions(npc: Npc):

    if npc.legendary_actions:
        actions = "### Legendary Actions\n"
        for action in npc.legendary_actions:

            action = f"***{action.name}*** {action.effect}\n:\n"
            actions = actions + action
        return actions
    else:
        return ""
