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

    show cassin dark at center
    show cassin with dis

    # These display lines of dialogue.

    cs "啊咧？应该是丢在这个垃圾箱里没错…"

    hide cassin
    show long_island at left, bobble1

    li "里面空空如也，一定已经被回收了"

    hide cassin
    show laffey at right
    show long_island dark with dis

    la "那，要去废弃场看看吗？"

    hide long_island
    show cassin at left
    show laffey dark with dis

    cs "嗯…记得这里的垃圾为了鉴别可回收物品，不是会先运到明石那里去的吗？"

    hide cassin
    show long_island at left, bobble1

    li "那么，就朝明石那里突击！"

    show laffey at right, bobble1
    show long_island dark with dis

    la "噢~"

    scene bg room7 with Fade(2, 2, 2)

    show long_island at left

    li "看到明石的店了，最后一站了！"

    show laffey at center
    show laffey at moveR
    show long_island dark with dis

    la "到达，拉菲第一个到达"

    hide laffey
    show long_island at moveR

    li "太可惜了，第二个到达吗"

    show cassin at moveL
    show long_island dark with dis

    cs "第三个到达，刚醒就全力疾走什么的能饶了我吗"

    hide long_island
    hide cassin
    show akashi at right

    ak "啊喵？欢迎光临喵~大家这么急是为什么？"

    hide cassin
    show laffey at left
    show akashi dark with dis

    la "在赛跑"

    hide laffey
    show cassin at left
    show akashi dark with dis

    cs "额不对吧"

    hide cassin
    show long_island at left, bobble1

    li "啊，对了！长岛我们是来找紫色的蘑菇的。"
    li "应该是和垃圾一起运过来的，明石你知道吗？"

    show akashi at right, shake1
    show long_island dark with dis

    ak "蘑菇？莫非是指这个吗？"

    hide long_island
    show laffey at left, bobble1
    show akashi dark with dis

    la "啊，发现睡眠蘑菇"

    hide laffey
    show long_island at left, shake2

    li "果然有，还回来还回来"

    show akashi at right, shake1
    show long_island dark with dis

    ak "才不要，这已经是明石的东西了"

    hide long_island
    show cassin at left
    show akashi dark with dis

    cs "为什么？没吃完的蘑菇也没办法当商品吧"

    show akashi at right
    show cassin dark with dis

    ak "呵呵呵，藏着也没用喵，明石我知道这不是简单的蘑菇喵~"

    hide cassin
    show long_island at left, bobble1
    show akashi dark with dis

    li "为…为什么会知道这个"

    show akashi
    show long_island dark with dis

    ak "这个反应，果然预想是对的喵~"

    show long_island
    show akashi dark with dis

    li "被……被套话了吗？"

    hide long_island
    show laffey at left

    la "长岛真是不注意"

    show akashi
    show laffey dark with dis

    ak "不用那么消沉喵~明石我本来就在找蘑菇喵~"

    hide laffey
    show cassin at left
    show akashi dark with dis

    cs "莫非，明石也听了那个传言？"

    show akashi
    show cassin dark with dis

    ak "当然喵~明石可是这个基地第一的情报通~圣地亚哥培养的蘑菇里有BUST UP效果的事喵~"

    hide cassin
    show long_island at left, bobble1
    show akashi dark with dis

    li "不愧是明石~长岛和愉快的小伙伴们正在寻找BUST UP蘑菇的冒险中~"

    show akashi
    show long_island dark with dis

    ak "也就是，这个蘑菇就是目的喵？太好了，效果要是真的话那就大受欢迎了~"

    hide long_island
    show laffey at left
    show akashi dark with dis

    la "不是，这是吃了会睡觉的蘑菇"

    hide laffey
    show cassin at left

    cs "刚才，拉菲不是说了睡眠蘑菇吗？"

    show akashi at right, bobble1
    show cassin dark with dis

    ak "虾米？真的喵？"

    hide cassin
    show long_island at left
    show akashi dark with dis

    li "觉得是骗你的话吃一下试试就好啊，一口就咕咚歇菜了"

    show akashi
    show long_island dark with dis

    ak "嗯……不像假话的样子，试一下就算了，但是，如果这样为什么需要这个蘑菇呢？"

    hide long_island
    show laffey at left
    show akashi dark with dis

    la "埃尔德里奇吃了舞蹈蘑菇霹雳霹雳放电，为了让她冷静下来，需要睡眠蘑菇"

    hide laffey
    show cassin at left

    cs "似乎，两种蘑菇的效果能互相抑制的样子"

    show akashi
    show cassin dark with dis

    ak "这样的话那就没办法了，这个蘑菇就还给你们了"
    ak "但是有一个条件喵"

    hide cassin
    show laffey at left
    show akashi dark with dis

    la "条件？" 

    show akashi
    show laffey dark with dis

    ak "如果得到BUST UP蘑菇的话，希望能让给我一片喵~"

    hide laffey
    show long_island at left, bobble1
    show akashi dark with dis

    li "这种程度的话OK啦~"

    show long_island at left, shake1

    li "那么，睡眠蘑菇就拿去埃尔德里奇那里了~"

    show akashi at moveL
    show long_island dark behind akashi

    ak "呀，慢着喵~"

    show cassin at right
    show akashi dark

    cs "还有什么事吗？"

    hide long_island
    hide cassin
    show akashi at moveR

    ak "提问！你们知道传言的出处吗？"

    show laffey at left
    show akashi dark with dis

    la "是指BUST UP蘑菇的事？拉菲我不知道哦~"

    hide laffey
    show long_island at left

    li "长岛也只是听到别人在谈而已"

    show akashi
    show long_island dark with dis

    ak "这样的话就由我情报通明石来提供一个特大帮助吧~这个情报的出处似乎是海伦娜的样子喵~"

    hide long_island
    show laffey at left
    show akashi dark

    la "海伦娜？"

    show akashi
    show laffey dark with dis

    ak "没错喵~早上有人发现海伦娜的胸变大了去追问她"
    ak "然后海伦娜是这样回答的：“因为吃了圣地亚哥的蘑菇”这样的喵~"

    show laffey at moveL, grabL
    pause 0.1
    show long_island at moveL, grabL
    pause 0.1
    show cassin at moveL, grabL

    ak "呀呀？"

    scene bg room3 with Fade(1, 1, 1)
    show light at reset, spark
    with Dissolve(1)

    "（脚步声……）"

    show mccall at right

    mc "啊，大家好像回来了的样子"

    hide mccall
    show laffey at moveL
    pause 0.05
    show long_island at moveL
    pause 0.05
    show cassin at moveL
    pause 0.5

    hide laffey
    hide long_island
    hide cassin
    show san_diego at right, dance

    sd "欢迎回来~欢迎的，舞蹈~睡眠蘑菇找到了吗？"

    show laffey at left, bobble1
    show san_diego dark with dis

    la "嗯，拿到了~"

    hide laffey
    show cassin at left

    cs "但是，要怎样拿给埃尔德里奇呢？房间里霹雳霹雳的进不去"

    hide cassin
    show long_island at left, shake2

    li "没事，接下来就交给幽灵小姐吧~"

    show san_diego
    show long_island dark at left with dis

    sd "噢~长岛振臂高挥起来了"

    show long_island
    hide san_diego

    li "上了哦，埃尔德里奇，把嘴张大~"

    hide long_island
    show eldridge at center, bobble1

    el "了…啊"

    hide eldridge
    show long_island at left, shake1

    li "看好了，这就是？？？？？，技术球投法哦"

    window hide
    show long_island at left, shake1
    pause 1
    hide long_island
    show eldridge at center, bobble1
    pause 1
    hide eldridge
    show long_island at left, bobble1

    li "好球！"

    show mccall at right
    show long_island dark with dis

    mc "蘑菇塞进了埃尔德里奇的嘴里……"

    hide mccall
    hide long_island
    show eldridge at center, bobble2
    pause 3
    hide light

    pause

    hide eldridge
    show laffey at left

    la "啊，霹雳霹雳停下来了"

    show cassin at right
    show laffey dark with dis

    cs "剩下的也给圣地亚哥吧"

    hide laffey
    show san_diego at left, dance
    show cassin at right, shake1
    pause 0.5
    show san_diego at left, bobble2

    sd "啊…舞蹈激情要沉下去了…啊，总觉得变得寂寞起来了"

    hide cassin
    show mccall at right
    show san_diego dark at left

    mc "还恋恋不舍的…"

    hide san_diego
    hide mccall
    show eldridge at center

    el "埃尔德里奇……好累…放电太多了，好疲惫"
    el "所以，谢谢你们来救我"

    hide eldridge
    show long_island at left, shake1

    li "不用介意啦，有困难的时候就互相帮忙嘛~"
    li "但是果然这里也没有BUST UP蘑菇的样子……"

    show mccall at right
    show long_island dark with dis

    mc "那要去party最后一位出席者海伦娜那里看一下吗？"

    show long_island at left, bobble1
    show mccall dark with dis

    li "对了，根据明石的话说，传言的出处是海伦娜那里，这次应该真的能找到BUST UP蘑菇了"

    hide long_island
    show laffey at left, shake1

    la "嗯……"

    show mccall
    show laffey dark

    mc "怎么了拉菲？"

    show laffey
    show mccall dark

    la "拉菲和海伦娜一个房间，但是没有察觉到胸的事"

    hide mccall
    show san_diego at right
    show laffey dark with dis

    sd "是不是真的看了就知道了~"

    show san_diego at right, bobble1

    sd "那么，大家一起朝着最后的目的地出发！"

    hide laffey
    show long_island at left, shake1

    li "啊……别抢我出发的信号啊！"

    show long_island at left, shake2

    li "这个冒险的领导是长岛啊！"

    hide long_island
    hide san_diego
    show eldridge at right

    el "埃尔德里奇也一起？"

    show cassin at left
    show eldridge dark

    cs "虽然不是很明白，是这种氛围。而且一起来的话胸也许会变大…"

    hide cassin
    show san_diego at left, shake1

    sd "大丰胸，让指挥官神魂颠倒地出现~"

    show eldridge
    show san_diego dark with dis

    el "指挥官？我知道了"

    show light at reset, spark behind eldridge
    show eldridge at right, bobble2

    el "我去"

    hide eldridge
    show mccall at right

    mc "埃尔德里奇拿出干劲又霹雳霹雳放电了……"

    show san_diego at left, shake2
    show mccall dark

    sd "哔哔哔哔要麻了要麻了…但是这个溢出的激情是…"

    show san_diego at left, shake2
    pause 0.2
    show san_diego at left, dance

    sd "来了来了，我还能跳舞~~"

    hide mccall
    show laffey at right
    show san_diego dark

    la "啊，又发作了"

    hide laffey
    show mccall at right

    mc "这个我想大概是她自己想跳而已"

    scene black with Dissolve(8)

    # This ends the game.

    return
