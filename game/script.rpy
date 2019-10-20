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

    "(脚步声)"

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
    pause

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

    cs "(zzZ)"

    show long_island at left, fallR
    li "呀！"

    show long_island dark with dis
    cs "(zzZ)"

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

    cs "(zzZ zzZ)"

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
    show san_diego at right, dance
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

    la "嗯，和那个故事一样的话，睡美人公主亲一下就会醒，应该"

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

    cs "嗯……啊~"
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

    sd "耶~结果挺好的嘛，高兴的，舞蹈~"

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

    li "都到这里了，就尽情增加同伴了，不准反驳"

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

    mc "更吵了……"

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

    scene bg home with Fade(2, 2, 2)
    show light at reset, spark
    with Dissolve(1)
    "(电流声……)"
    show long_island at left, shake1

    li "嗯……下一个找埃尔德里奇吗？"

    show mccall at right
    show long_island dark with dis

    mc "蘑菇party的出席者还有两位，本来是想着就近先找埃尔德里奇的……是不是出了什么问题了"

    show long_island at left, bobble1
    show mccall dark with dis

    li "问题大了去了……门缝里都霹雳霹雳地传出了不得了的声音和光线了，肯定不是小事"

    hide mccall
    show cassin at right
    show long_island dark with dis

    cs "好耀眼，刚睡醒遭不住啊"

    hide long_island
    show laffey at left
    show cassin dark with dis

    la "卡辛还很困吗"

    hide cassin
    show san_diego at right, dance
    show laffey dark with dis

    sd "哈哈哈是火花~踩着霹雳霹雳的节奏，跳舞吧~"

    hide laffey
    show long_island at left, shake1
    show san_diego dark with dis

    li "圣地亚哥，趁着这气势把门打开，幽灵小姐害怕得不敢接近"

    show san_diego
    show long_island dark with dis

    sd "OK！交给我吧，舞蹈攻击~~~~~~"
    hide long_island
    show san_diego at moveL, dance

    pause 1
    show laffey at right, shake1
    show san_diego dark

    la "哇，圣地亚哥旋转着朝着门去了"

    show san_diego
    show laffey dark with dis

    sd "上了，开门……哇哇哇！！"

    show san_diego at left, dance

    sd "哇哇哇，哔哩哔哩~~~~~来了……"

    hide laffey
    show mccall at right
    show san_diego dark with dis

    mc "直接被电击命中"

    show san_diego dark at left, fallR
    show mccall

    mc "啊，倒了"

    hide mccall
    show long_island at center
    pause 0.1
    show long_island at moveL

    li "圣地亚哥！！！啊，悲剧啊！"
    li "但是大家，现在不能哭，门已经开了，长岛我们要把同伴伟大的牺牲刻在胸膛，朝前进发"

    show laffey at right
    hide long_island
    show san_diego dark at left, shake1

    la "拉菲并没有在哭，而且圣地亚哥霹雳霹雳地还在动"

    hide laffey
    show mccall at right

    mc "大概只是晕了吧"

    hide san_diego
    show cassin at left
    show mccall dark with dis

    cs "趁着功夫，我也睡一觉可以吗"

    hide cassin
    show long_island at left, shake1

    li "不能浪费圣地亚哥的牺牲，大家一起去确认埃尔德里奇的样子"

    hide mccall
    show laffey at right
    show long_island dark with dis

    la "但是这样，也没办法进去里面啊"

    show long_island at left, shake1
    show laffey dark with dis

    li "通过门缝偷偷地观察里面的情况"

    hide laffey
    show mccall at right

    mc "确实也不该放着她不管，卡辛，加油吧"

    hide long_island
    show cassin at left
    show mccall dark with dis

    cs "麦考尔都发生了这么多事还那么有干劲，虽然事情我粗略听了，你就这么想让胸变大吗"

    show mccall
    show cassin dark with dis

    mc "不…不是啦，我只是好奇传言是不是真的而已"

    show cassin at left, shake1
    show mccall dark with dis

    cs "嗯……"

    hide cassin
    show laffey at left, shake1

    la "拉菲我想让胸变大起来看指挥官什么反应，他要是喜欢的话我会很高兴的，大概"

    hide laffey
    show cassin at left

    cs "拉菲真是坦率"

    show mccall
    show cassin dark with dis

    mc "能别说得仿佛我很不坦率的样子吗。话说回来现在比起这个更重要的是埃尔德里奇啊"

    hide cassin
    show long_island at left, shake1
    show mccall dark with dis

    li "大家快看，房间的深处"

    hide mccall
    show laffey at right
    show long_island dark with dis

    la "埃尔德里奇，找到了"

    hide laffey
    show cassin at right

    cs "普通地站着啊，为什么这么霹雳霹雳地放电呢"

    show long_island at left, bobble1
    show cassin dark with dis

    li "喂，埃尔德里奇~~~~~~~"

    hide cassin
    show long_island

    scene bg room3
    show light at reset, spark

    show eldridge at center, bobble2

    el "嗯？早上……好~~"

    hide eldridge

    show long_island at left, shake1

    li "埃尔德里奇只是朝这边看过来，霹雳霹雳暴走起来了"

    show cassin at right
    show long_island dark with dis

    cs "埃尔德里奇，究竟怎么了"

    hide cassin
    hide long_island

    show eldridge at center

    el "不知道，放电一直停不下来，就在房间里面呆着了"

    hide eldridge
    show laffey at right, bobble1

    la "啊，埃尔德里奇的旁边，有没吃完的蘑菇"

    hide eldridge
    show mccall at left
    show laffey dark with dis

    mc "真的，那个颜色是跳舞蘑菇吧"

    hide laffey
    show long_island at right
    show mccall dark with dis

    li "但是，埃尔德里奇没有在跳舞啊"

    hide mccall
    show cassin at left
    show long_island dark with dis

    cs "嗯……仔细看，埃尔德里奇的手微妙地在动着"

    hide long_island
    show laffey at right, shake1
    show cassin dark with dis

    la "啊，拉菲稍微来试探一下"

    hide cassin
    show mccall at left
    show laffey dark with dis

    mc "试探？"

    show laffey
    show mccall dark

    la "嗯。"

    hide mccall
    show laffey at moveC, bobble1

    la "埃尔德里奇，Yeah!"

    hide laffey
    show eldridge at center, bobble1

    el "Yeah!"

    hide eldridge
    show laffey at right

    la "嗯，没有错，埃尔德里奇在踩着旋律"

    show long_island at left, bobble1
    show laffey dark with dis

    li "那个真的是在跳舞啊，吓一跳"

    hide long_island
    show san_diego at left, dance

    sd "嗯，埃尔德里奇也在跳舞？"

    show laffey
    show san_diego dark

    la "啊，圣地亚哥复活了"

    hide san_diego
    show mccall at left
    show laffey dark with dis

    mc "也就是说埃尔德里奇吃了跳舞蘑菇之后情绪高涨起来了"

    hide laffey
    show cassin at right
    show mccall dark

    cs "因为这个的原因霹雳霹雳放电停不下来"

    hide mccall
    show long_island at left, shake1
    show cassin dark with dis

    li "嗯……但是知道原因了也不知道要怎么办啊"

    hide cassin
    show san_diego at right, dance
    show long_island dark with dis

    sd "没事没事，虽然只是大概，吃紫色的蘑菇就好了"

    hide long_island
    show laffey at left
    show san_diego dark

    la "紫色是…睡眠蘑菇？"

    hide laffey
    show mccall at left

    mc "卡辛吃了睡着的那个是吧？"

    show san_diego
    show mccall dark

    sd "YES！其实我昨天也吃了跳舞蘑菇，但是那时什么都没有发生，一定是一起吃了紫色蘑菇的问题吧"

    hide mccall
    show long_island at left, bobble1
    show san_diego dark

    li "对啊，让人情绪高涨不禁想跳舞的蘑菇，以及让人沉睡的蘑菇，一定是两种蘑菇功效抵消了"

    hide san_diego
    show laffey at right
    show long_island dark with dis

    la "那，应该回卡辛的房间，把睡眠蘑菇拿过来才行"

    hide laffey
    show cassin at right

    cs "啊，那个蘑菇在过来的途中我扔掉了"

    show long_island at left, bobble1
    show cassin dark

    li "为什么啊！！"

    show cassin
    show long_island dark with dis

    cs "因为，以为是危险品……"

    hide long_island
    show laffey at left
    show cassin dark with dis

    la "确实，吃了很危险"

    hide laffey
    show long_island at left
    show cassin dark with dis

    li "现在马上去回收"
    pause 0.5
    show long_island at moveR
    li "卡辛，跟上来"

    show cassin
    show long_island dark behind cassin

    cs "啊，别拖我啊"

    show laffey at left
    show cassin dark

    la "拉菲也去"

    hide long_island
    hide cassin
    hide laffey
    show mccall at right

    mc "那我就和圣地亚哥一起留在这里看着埃尔德里奇的情况"

    show san_diego at left, dance
    show mccall dark with dis

    sd "加油哦！Fight！"

    hide san_diego
    hide mccall
    show eldridge at center

    el "慢走…等你们"

    hide eldridge
    show cassin at right
    show long_island at center

    li "最大船速，跑起！"
    pause 1.3
    show cassin at grabR
    show long_island at grabR
    pause 0.2
    show laffey at center
    pause 0.2
    show laffey at grabR

    scene black with Dissolve(5)

    # This ends the game.

    return
