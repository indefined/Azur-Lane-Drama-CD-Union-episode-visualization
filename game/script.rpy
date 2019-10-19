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

    "(敲门声)"

    show long_island dark at center
    show long_island with dis

    # These display lines of dialogue.

    li "到达卡辛的船坞了~"

    show long_island at moveL
    show long_island dark with dissolve
    show long_island dark at moveL_after
    show san_diego dark at right, dance
    show san_diego with dis

    sd "嘿嘿，来跳舞~"

    hide long_island
    show laffey at left
    show san_diego dark with dis

    la "圣地亚哥…一边跳舞一边在敲门"

    hide san_diego
    show mccall at right
    show laffey dark with dis

    mc "邀请她来跳舞是要闹哪样…"

    hide laffey
    show long_island at left, bobble1
    show mccall dark with dis

    li "是啊，重点不对啊！"
    li "卡辛，关于蘑菇有事找你，开下门~"

    hide mccall
    show san_diego at right, dance
    show long_island dark with dis

    sd "啊对，我们是来找BUST UP蘑菇的~"
    show san_diego at right, shake2
    sd "嘿嘿，开门开门~"
    show san_diego dark at right, dance

    hide long_island
    show laffey at left

    la "没反应"

    hide san_diego
    show long_island at right
    show laffey dark with dis

    li "奇怪，休息时间她应该是宅在船坞里才对"

    hide laffey
    show mccall at left
    show long_island dark with dis

    mc "是不是蛰伏状态被打扰不高兴了"

    show long_island
    show mccall dark with dis

    li "唔…好像很可能的样子…"
    li "同为家里蹲的我很能理解…"

    hide mccall
    show san_diego at left, shake1
    show long_island dark with dis

    sd "没有锁门哦"

    show san_diego dark at left, dance
    show long_island

    li "真的？"

    hide san_diego
    show laffey at left
    show long_island dark with dis

    la "但是，里面漆黑一片"

    hide long_island
    show mccall at right
    show laffey dark with dis

    mc "是不是还在睡"

    hide laffey
    show san_diego at left, bobble1
    show mccall dark with dis

    sd "这种时候，就该啪啪的把灯打开~"

    scene bg room6

    hide san_diego
    show laffey at left

    la "卡辛她……倒在了地上"

    show mccall at right
    show laffey dark

    mc "旁边就是没吃完的蘑菇"
    mc "莫非是吃了那个……"

    hide laffey
    show long_island at left
    show mccall dark with dis

    li "莫非是毒蘑菇？"
    show long_island at left, shake2
    li "卡辛，你振作一点"

    hide mccall
    show long_island dark with dis

    cs "zzZ"

    show long_island at left, fallR
    li "呀！"

    show long_island dark with dis
    cs "zzZ"

    show san_diego at right, dance

    sd "哈哈哈，不过是在睡觉嘛"

    hide long_island
    show laffey at left
    show san_diego dark

    la "害我白操心"

    hide san_diego
    show mccall at right
    show laffey dark with dis

    mc "但是长岛都摔倒在她身上，完全没醒来"
    mc "而且圣地亚哥也一直蹦蹦哒哒地在跳舞…"

    hide laffey
    show long_island at left
    show mccall dark with dis

    li "痛痛痛，撞到鼻子了…"

    show long_island at left, shake2
    li "真是的，卡辛，起来啦！"

    hide mccall
    show long_island dark with dis

    cs "zzZ"

    show long_island

    li "诶？真的醒不来？"

    show mccall at right
    show long_island dark with dis

    mc "莫非，这是蘑菇的效果？"

    hide long_island
    show laffey at left
    show mccall dark with dis

    la "果然是毒蘑菇？"

    hide mccall
    show san_diego at right
    show laffey dark with dis

    sd "毒？啊，这和那个一样~"
    sd "就是那个，睡美人公主吃了毒苹果睡着的故事"

    hide laffey
    show long_island at left
    show san_diego dark with dis

    li "确实很像的感觉…那么毒倒是毒"
    li "名字就决定叫做，睡眠蘑菇吧"

    hide san_diego
    show mccall at right
    show long_island dark with dis

    mc "现在不是决定名字的时候呀，要是这样睡着不醒来的话怎么办"

    hide mccall
    show laffey at right

    la "拉菲我，可能知道怎么叫醒她"

    show long_island
    show laffey dark

    li "诶？真的？"

    show laffey
    show long_island dark

    la "嗯，和那个故事一样的话，睡美人公主亲一下就会醒"
    la "应该"

    hide long_island
    show mccall at left
    show laffey dark

    mc "亲……"

    hide laffey
    show san_diego at right, dance
    show mccall dark with dis

    sd "喔，拉菲，好主意，那么事不宜迟试一试吧"

    hide mccall
    show long_island at left, shake1
    show san_diego dark with dis

    li "试一试什么的……怎么说就算是幽灵也很害羞啊~"

    hide san_diego
    show mccall at right
    show long_island dark with dis

    mc "说到底亲一下就醒不过是故事里的事吧，常识来考虑的话不可能的啊"

    hide long_island
    show laffey at left
    show mccall dark with dis

    la "但是，这可是圣地亚哥培养的蘑菇哦"

    show mccall
    show laffey dark

    mc "迷之说服力……"

    hide laffey
    show long_island at left, shake2
    show mccall dark with dis

    li "但是果然……我还是做不到啦~"

    hide mccall
    show san_diego at right, dance
    show long_island dark with dis

    sd "大家都不做的话，那就我来吧"
    sd "一边跳舞，飞起来~"

    hide long_island
    show mccall at left
    show san_diego dark with dis

    mc "诶？这要怎样……"

    hide mccall
    show laffey at left

    la "啊，危险"

    show san_diego
    show laffey dark

    sd "啊，脚绊到了……"

    hide laffey
    show san_diego at moveL, fallL

    sd "哇哇哇哇哇……哇"

    show long_island at right
    show san_diego dark

    li "圣地亚哥螺旋俯冲着朝着卡辛的肚子撞了下去……"

    hide san_diego
    show laffey at left
    show long_island dark with dis

    la "暴击"

    hide long_island
    show mccall at right
    show laffey dark with dis

    mc "卡…卡辛……没事吧？"

    hide laffey
    show san_diego at left, dance
    show mccall dark with dis

    sd "呀，失败失败，反省的…舞蹈"

    hide san_diego
    show laffey at left

    la "跳着舞看着一点都没在反省"

    hide mccall
    show laffey dark with dis

    cs "咳…"

    show long_island at right

    li "看，卡辛吐出了什么东西来"

    show laffey
    show long_island dark with dis

    la "蘑菇的…碎片？"

    hide long_island
    show cassin at right
    show laffey dark with dis

    cs "啊~"
    cs "啊咧？大家，为什么？"

    hide laffey
    show mccall at left
    show cassin dark with dis

    mc "卡辛，太好了，醒过来了"

    hide cassin
    show long_island at right
    show mccall dark with dis

    li "一定是圣地亚哥的冲击让蘑菇吐了出来"

    hide mccall
    show san_diego at left, dance
    show long_island dark with dis

    sd "耶~结果挺好的呢，高兴的，舞蹈~"

    hide long_island
    show cassin at right
    show san_diego dark with dis

    cs "完全不知道是什么情况"

    hide san_diego
    show laffey at left
    show cassin dark with dis

    la "卡辛因为蘑菇睡死过去，圣地亚哥螺旋俯冲着把你弄醒了"

    hide laffey
    show mccall at left

    mc "不错的总结，拉菲"

    show cassin
    show mccall dark

    cs "说来，好像是只吃了蘑菇就睡着了的样子…"

    hide mccall
    show long_island at left, shake1
    show cassin dark with dis

    li "这个紫色蘑菇是睡眠蘑菇呢~"
    li "卡辛这里还有其它种类的蘑菇吗？长岛和愉快的小伙伴们正在找BUST UP蘑菇中"

    show cassin
    show long_island dark

    cs "没有了，我拿回来的就只有这个。说来……BUST UP蘑菇是……什么？"

    show long_island
    show cassin dark

    li "这个之后再跟你解释，总而言之卡辛也一起来"

    show cassin
    show long_island dark

    cs "诶？为什么？"

    show long_island
    show cassin dark

    li "到这里了，就尽情增加同伴了，不准反驳"

    show long_island at moveR
    pause 1

    show long_island at grabR
    show cassin at grabR
    cs "啊……咧……"

    hide long_island
    hide cassin
    show laffey at left

    la "卡辛被长岛拖走了，真可怜"

    show mccall at right
    show laffey dark with dis

    mc "怎么觉得，是不是有一半的目的变了……"

    hide laffey
    show san_diego at left, dance
    show mccall dark with dis

    sd "虽然不知道发生了什么，变得有趣起来了呢~嘿嘿嘿~"

    hide san_diego
    show laffey at left

    la "圣地亚哥飘起来了"

    show mccall
    show laffey dark

    mc "吵闹程度更进一步了……"

    hide laffey
    show san_diego at left, dance
    show mccall dark

    sd "Yeah! 来嘛，大家也一起踩上节奏~Here we come!"

    hide san_diego
    show laffey at left, bobble1

    la "Yeah!"

    show mccall
    show laffey dark

    mc "不用踩啦，好啦去下个地方吧"

    hide laffey
    hide mccall
    window hide


    scene black with Dissolve(2)

    # This ends the game.

    return
