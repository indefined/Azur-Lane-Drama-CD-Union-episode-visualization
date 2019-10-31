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
    show laffey at moveR with dis

    # These display lines of dialogue.

    cs "到达拉菲和海伦娜的房间了~大家，进来"

    scene bg room2 with Fade(1, 1, 1)

    show laffey at right

    li "海伦娜，我回来了"

    hide laffey
    show helena at right

    hl "拉菲，欢迎回来"
    hl "啊啦，怎么了？后面好像很多人的样子"

    show long_island at left, shake1
    show helena dark with dis

    li "我来打扰了"

    hide long_island
    show san_diego at left, dance

    sd "有事找海伦娜过来的哦~"

    show helena
    show san_diego dark with dis

    hl "找我？"

    hl "啊麦考尔和卡辛，连埃尔德里奇也在"

    hide san_diego
    show mccall at left

    mc "抱歉打扰你了，下次继续请你吃冰棒"

    hide mccall
    show cassin at left

    cs "事情完了就马上回去啊，我还想继续在船坞里睡觉……"

    hide cassin
    show eldridge at left

    el "盯~~~~~"

    show helena
    show eldridge dark with dis

    hl "为…为什么一直盯着我的胸呢？"

    show eldridge
    show helena dark with dis

    el "好大"

    show helena
    show eldridge dark with dis

    hl "是…是吗？我觉得挺普通的啊，比我大的孩子挺多的啊"

    hide eldridge
    show long_island at left
    show helena dark with dis

    li "盯~~~~~~~~~~~~"

    show helena
    show long_island dark with dis

    hl "连长岛也来，到底怎么了啦"

    show long_island
    show helena dark with dis

    li "虽然感觉是大了，想不起之前有多大，拉菲你怎么看？"

    hide long_island
    show laffey at left

    la "盯~~~~~~~~~~~~"

    show helena
    show laffey dark with dis

    hl "拉菲……"

    show laffey
    show helena dark with dis

    la "比早上看到的时候变大了，没有错"

    hide laffey
    show san_diego at left, dance

    sd "真的？那传言是真的啊，不愧是我养的蘑菇，耶耶耶~"

    hide san_diego
    show mccall at left

    mc "圣地亚哥好了别再跳了。但是这样的话这里应该有那个蘑菇吧？"

    hide mccall
    show light at reset behind helena
    show light at reset, spark
    show eldridge at left

    el "???"

    hide eldridge
    hide light
    show mccall at left

    mc "埃尔德里奇兴奋起来了，霹雳霹雳放电…"

    show helena
    show mccall dark with dis

    hl "等，等一下，究竟怎么了？大家眼神好可怕"

    hide mccall
    show long_island at left, bobble1
    show helena dark with dis

    li "呼呼呼，那是当然的啦~BUST UP蘑菇的效果被证明幽灵小姐也大开心"

    show helena
    show long_island dark with dis

    hl "BUST UP蘑菇？到底是……怎么回事？"

    show long_island at left, bobble1
    show helena dark with dis

    li "装傻也没用，你甲板都隆起来了"

    hide long_island
    show mccall at left

    mc "吃了圣地亚哥的蘑菇胸变大起来的对吧？"

    hide mccall
    show laffey at left

    la "从明石那里听到的你说过这话"

    hide laffey
    show cassin at left

    cs "还有没有剩下的？"

    hide cassin
    show san_diego at left, dance

    sd "大家都想吃BUST UP蘑菇然后向指挥官表现呢"

    show helena
    show san_diego dark with dis

    hl "啊，是这回事啊……但是，那个…………"

    hide san_diego
    show eldridge at left
    show helena dark with dis

    el "全部吃了？"

    hide eldridge
    show mccall at left

    mc "确实没看见呢"

    show helena
    show mccall dark with dis

    hl "不是，吃了蘑菇胸变大的事……只是玩笑而已。一般考虑的话，怎么可能会有这种事？"

    hide mccall
    show laffey at left
    show helena dark with dis

    la "但是，确实大起来了。拉菲一直和海伦娜一起睡所以很清楚"
    la "摸一下的话，就更清楚了"

    show helena at right, shake1
    show laffey dark with dis

    hl "拉…拉菲，现在不行啊"

    hide laffey
    show long_island at left, bobble1
    show helena dark with dis

    li "啊，把胸藏起来了好可疑！"

    show long_island at left, shake1

    li "一定是把蘑菇藏在变大的胸里"

    show helena
    show long_island dark with dis

    hl "不…不是啦，不要说奇怪的话"

    show long_island at left
    show helena dark with dis

    li "那么，就来摸一摸确认一下！"

    show long_island at moveR
    pause 1
    show long_island dark behind helena at moveR_after
    show helena

    hl "SG，借我力量！"

    show helena dark at moveL
    pause 0.6
    show long_island at right, fallR
    pause 1
    hide long_island
    show long_island at right

    li "完美的回避，行动完全被看穿了"

    hide long_island
    show san_diego at right, dance

    sd "那么，接下来就由我上哦~必杀！圣地亚哥攻击~~~~~~~"

    show san_diego at moveL
    pause 1
    show san_diego dark behind helena
    show helena

    hl "看到了哦"

    show helena dark at moveR
    pause 0.4
    show san_diego dark at left, fallL
    pause 0.6
    show san_diego at left, dance

    sd "竟然能看穿这个行动，不赖嘛"

    hide san_diego
    show mccall at left

    mc "不愧是SG，高性能雷达的性能力量啊"

    hide mccall
    show cassin at left

    cs "麦考尔吃着冰棒完全就是看戏状态了"

    hide cassin
    show mccall at left

    mc "卡辛你才是完全0干劲吧"

    hide mccall
    show cassin at left

    cs "因为已经看到结果了，就算是海伦娜的SG"

    hide cassin
    show long_island at left, bobble1

    li "没错，雷达就用埃尔德里奇的放电来干扰"

    show eldridge dark at right behind helena
    show long_island dark with dis
    show helena

    hl "啊，埃尔德里奇，什么时候到了后面…"

    show light behind eldridge
    show light at reset, spark
    show helena dark behind eldridge
    show eldridge

    el "触摸~"

    hide light
    hide long_island
    show helena at moveL

    hl "我还没放弃呢"

    hide eldridge
    show san_diego at right, dance
    show helena dark with dis

    sd "好强，回转身体错开了埃尔德里奇的触摸"

    show helena
    show san_diego dark with dis

    hl "就这样逃出房间……额"

    show laffey dark at left behind helena
    show laffey
    show helena dark behind laffey

    la "抓住海伦娜了"

    hide san_diego
    show long_island at right, bobble1
    show laffey dark

    li "拉菲，NICE~在海伦娜调整形式的时候很好的迂回过去了"

    hide long_island
    show san_diego at right, dance

    sd "那么，从海伦娜的胸里把BUST UP蘑菇掠夺出来吧"

    show laffey at left, shake2
    show san_diego dark with dis

    la "嗯？"



    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""



    scene black with Dissolve(8)

    # This ends the game.

    return
