from pathlib import Path
from npc import Npc


def build_stat_block(npc: Npc):
    abilities = build_abilities(npc)
    actions = build_actions(npc)
    legendary_actions = build_legendary_actions(npc)
    bonus_actions = build_bonus_actions(npc)
    spellcasting = build_spellcasting(npc)
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
**Damage Immunities**    :: {npc.damage_immunities}
**Damage Resistances**   :: {npc.damage_resistances}
**Senses**               :: {npc.senses}
**Languages**            :: {npc.languages}
**Challenge**            :: {npc.challenge_rating}
___
{abilities}
{spellcasting}
### Actions
{actions}
{bonus_actions}
{legendary_actions}

"""
    Path("npcs").mkdir(exist_ok=True)
    file_name = f"npcs\\{npc.name}"
    with open(file_name, "w") as f:
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


def build_spellcasting(npc: Npc):

    if not npc.spellcasting:
        return ""
    spellcasting = npc.spellcasting
    result = f"***Spellcasting*** {spellcasting.details}\n"
    result += f"::*Spell slots* {spellcasting.spell_slots}\n"
    if spellcasting.cantrips:
        result += f"::*Cantrips* {', '.join(spellcasting.cantrips)}\n"
    if spellcasting.level_1:
        result += f"::*Level 1* {', '.join(spellcasting.level_1)}\n"
    if spellcasting.level_2:
        result += f"::*Level 2* {', '.join(spellcasting.level_2)}\n"
    if spellcasting.level_3:
        result += f"::*Level 3* {', '.join(spellcasting.level_3)}\n"
    if spellcasting.level_4:
        result += f"::*Level 4* {', '.join(spellcasting.level_4)}\n"
    if spellcasting.level_5:
        result += f"::*Level 5* {', '.join(spellcasting.level_5)}\n"
    if spellcasting.level_6:
        result += f"::*Level 6* {', '.join(spellcasting.level_6)}\n"
    if spellcasting.level_7:
        result += f"::*Level 7* {', '.join(spellcasting.level_7)}\n"
    if spellcasting.level_8:
        result += f"::*Level 8* {', '.join(spellcasting.level_8)}\n"
    if spellcasting.level_9:
        result += f"::*Level 9* {', '.join(spellcasting.level_9)}\n"
    result += ":\n"
    return result


def build_legendary_actions(npc: Npc):

    if npc.legendary_actions:
        actions = "### Legendary Actions\n"
        for action in npc.legendary_actions:

            action = f"***{action.name}*** {action.effect}\n:\n"
            actions = actions + action
        return actions
    else:
        return ""
