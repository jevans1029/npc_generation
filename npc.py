from pydantic import BaseModel
from typing import List, Optional


class Abilities(BaseModel):
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int


class Action(BaseModel):
    # description: str
    name: str
    # recharge: Optional[str]
    # saving_throw: Optional[str]
    # attack_bonus: Optional[int]
    # damage: Optional[str]
    effect: str


class Spellcasting(BaseModel):
    details: str
    cantrips: Optional[List[str]]
    level_1: Optional[List[str]]
    level_2: Optional[List[str]]
    level_3: Optional[List[str]]
    level_4: Optional[List[str]]
    level_5: Optional[List[str]]
    level_6: Optional[List[str]]
    level_7: Optional[List[str]]
    level_8: Optional[List[str]]
    level_9: Optional[List[str]]


class SpecialAbility(BaseModel):
    name: str
    effect: str


class LegendaryAction(BaseModel):
    name: str
    effect: str


class Npc(BaseModel):
    name: str
    description: str
    creature_type: str
    armor_class: int
    movement_speed: str
    abilities: Abilities
    hitpoints: str
    condition_immunities: Optional[str]=""
    damage_immunities: Optional[str]=""
    damage_resistances: Optional[str]=""
    senses: str
    languages: str
    proficiency_bonus: int
    saving_throw_proficiencies: List[str]
    skill_proficiencies: List[str]
    spellcasting: Optional[Spellcasting]=None
    special_abilities: Optional[List[SpecialAbility]]
    actions: List[Action]
    bonus_actions: Optional[List[Action]]
    legendary_actions: Optional[List[LegendaryAction]]
    challenge_rating: int
