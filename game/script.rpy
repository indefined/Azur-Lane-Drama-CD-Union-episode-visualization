# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define la = Character(_("Laffey"), color="#AAED60")
define mc = Character(_("McCall"), color="#AAED60")
define li = Character(_("Long Island"), color="#AAED60")
define sd = Character(_("San Diego"), color="#AAED60")
define cs = Character(_("Cassin"), color="#AAED60")
define el = Character(_("Eldridge"), color="#AAED60")
define hl = Character(_("Helena"), color="#AAED60")
define ak = Character(_("Akashi"), color="#AAED60")


# The game starts here.

default box = 1

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    window hide
    scene black
    show opening_text _("Azur Lane Drama CD Union Episode\n\n") with Dissolve(2)
    hide opening_text with Dissolve(2)
    scene bg home
    show next at next_prompt, next_prompt_animation onlayer ontop
    with Dissolve(2)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show laffey dark at center
    show laffey with dis

    # These display lines of dialogue.

    scene black with Dissolve(2)

    # This ends the game.

    return
