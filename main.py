from chat_completion import generate_npc
from markdown import build_stat_block

# Change this
DESCRIPTION = "a goblin chieftain that knows a bit of magic"

if __name__ == "__main__":
    npc = generate_npc(DESCRIPTION)
    print(npc.model_dump_json(indent=2))
    build_stat_block(npc)
