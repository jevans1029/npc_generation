from chat_completion import generate_npc
from markdown import build_stat_block

# Change this
DESCRIPTION = "a goblin"

if __name__ == "__main__":
    npc = generate_npc(DESCRIPTION)
    build_stat_block(npc)
