# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals

import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton, CarouselContainer
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)
list=[]

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)
    
 
    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if isinstance(event, FollowEvent):
            profile = line_bot_api.get_profile(event.source.user_id)
            print(profile.display_name)
            print(profile.user_id)
            print(profile.picture_url)
            print(profile.status_message)
            list.append(event.source.user_id)
            print(list)
            message = TextSendMessage(text='請輸入與從者相對應的編號以進行檢索:\n1. 阿爾托莉亞_アルトリア (Saber)\n2. 阿提拉_アルテラ\n3. 吉爾伽美什_ギルガメッシュ(Archer)\n4. 諸葛孔明〔艾梅洛II世〕\n5. 坂田金時\n6. 弗拉德三世\n7. 貞德\n8. 俄里翁\n輸入"目錄" 或 "menu" 以重新呼叫此條目')
            line_bot_api.reply_message(event.reply_token, message)
        
        if isinstance(event, UnfollowEvent):
            print(list[0])
            list.remove(event.source.user_id)
        if isinstance(event, JoinEvent):
            profile = event.source.group_id
            print(profile)
            list.append(event.source.group_id)
            print(list)
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='group joined'))
          
        if isinstance(event, MessageEvent):
            text = event.message.text
            if text == '目錄' or text.lower() == 'menu'.lower():
                
                message = TextSendMessage(text='請輸入與從者相對應的編號以進行檢索:\n1. 阿爾托莉亞_アルトリア (Saber)\n2. 阿提拉_アルテラ\n3. 吉爾伽美什_ギルガメッシュ(Archer)\n4. 諸葛孔明〔艾梅洛II世〕\n5. 坂田金時\n6. 弗拉德三世\n7. 貞德\n8. 俄里翁\n輸入"目錄" 或 "menu" 以重新呼叫此條目')
                line_bot_api.reply_message(event.reply_token, message)
          
            elif text == '推':
                print(list)
                line_bot_api.multicast(list, TextSendMessage(text='fadachai'))
                    
              #  line_bot_api.multicast(list, TextSendMessage(text='fadachai'))
            #arutoria penderagon(saber)
            elif text == '1':
                bubble = BubbleContainer(
                        direction='ltr',
                        header=BoxComponent(
                            layout='vertical',
                            contents=[TextComponent(text='阿爾托莉亞 (Saber)', align='center')
                            ]
                        ),
                        hero=ImageComponent(url='https://i.imgur.com/EcL4D2Q.jpg',size='full',margin='md',aspect_ratio='16:9',aspect_mode='cover'),
                        body=BoxComponent(layout='horizontal',spacing='md',
                            contents=[
                                BoxComponent(layout='vertical',flex=0,
                                    contents=[  
                                        TextComponent(text='寶具', weight='bold'),
                                        ImageComponent(url='https://i.imgur.com/4jsuoW8.jpg',align='start',size='xs'
                                        ),
                                        TextComponent(text='保有技能', weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_300.png',margin='xxl',size='xs',align='start'
                                        ),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_306.png',margin='xxl',size='xs',align='start'
                                        ),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_603.png',margin='xxl',size='xs',align='start'
                                        ),
                                        TextComponent(text='↓強化後',align='center'
                                        ),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_601.png',size='xs', align='start', margin='xxl'
                                        ),
                                        TextComponent(text='職階技能', weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_100.png',margin='xxl',size='xs',align='start'
                                        ),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_102.png',margin='xxl',size='xs',align='start'
                                        ),
                                        
                                    ]
                                ),
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='約束された勝利の剣',size='md', color='#FF0000'),
                                        TextComponent(text='對敵全體攻擊 400%-500%[Lv.]' ,size='xs'),
                                        TextComponent(text='自身NP再累積 20%-50%[Oc]' ,size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='カリスマ B',size='xs'),
                                        TextComponent(text='全體攻擊力上升 9% ~ 18%',size='xs'),
                                        TextComponent(text='持續3回合',size='xs'),
                                        TextComponent(text='CD : 7 → 5',size='xs'),
                                        SeparatorComponent(margin='lg', color='#FFFFFF'),
                                        TextComponent(text='魔力放出 A',size='xs'),
                                        TextComponent(text='自身的B卡性能提升 30% - 50%',size='xs'),
                                        TextComponent(text='持續1回合',size='xs'),
                                        TextComponent(text='CD : 7 → 5',size='xs'),
                                        SeparatorComponent(margin='xl', color='#FFFFFF'),
                                        TextComponent(text='直感 A',size='xs'),
                                        TextComponent(text='星星大量獲得  5 - 15',size='xs'),
                                        TextComponent(text='CD : 7 → 5',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='輝ける路 EX',size='xs'),
                                        TextComponent(text='自身的NP增加 20% - 30%',size='xs'),
                                        TextComponent(text='星星大量獲得 5 - 15',size='xs'),
                                        TextComponent(text='CD 7 → 5',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xl', color='#FFFFFF'),
                                        TextComponent(text='対魔力 A', size='xs'),
                                        TextComponent(text='自身的弱體耐性提升20%', size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xs', color='#FFFFFF'),
                                        TextComponent(text='騎乗 B', size='xs'),
                                        TextComponent(text='自身的Quick卡性能提升：8%', size='xs'),
                                        
                                       
                                    ]
                                )
                            ]
                        ),
                        footer=BoxComponent(
                            layout='horizontal',
                            contents=[
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        TextComponent(text='技能優先度 :',weight='bold'),
                                        TextComponent(text='強化前 : 1 = 2 > 3'),
                                        TextComponent(text='強化後 : 3 > 1 = 2'),
                                        TextComponent(text='簡評 :', weight='bold',),
                                        TextComponent(text='阿爾托莉亞在強化祖傳廢技直感為充'),
                                        TextComponent(text='能之後，正式一躍成為周回家族的一'),
                                        TextComponent(text='員，加上一技和二技都是強化輸出的'),
                                        TextComponent(text='技能讓她在周回的時候能打足傷害，'),
                                        TextComponent(text='但論高難度關卡以阿爾托莉亞的技能'),
                                        TextComponent(text='組來說還是有點勉強。'),
                                    ]
                                )
                             ]
                         )
                 )
                message = FlexSendMessage(alt_text=text, contents=bubble)
                line_bot_api.reply_message(event.reply_token, message)
            #altera        
            elif text == '2':
                bubble = BubbleContainer(
                        direction='ltr',
                        header=BoxComponent(
                            layout='vertical',
                            contents=[TextComponent(text='阿提拉_アルテラ', align='center')
                            ]
                        ),
                        hero=ImageComponent(url='https://media1.tenor.com/images/862030c843d89b2a1df48fc6bc8b6fea/tenor.gif?itemid=13246388',size='full',margin='md',aspect_ratio='16:9',aspect_mode='cover'),
                        body=BoxComponent(layout='horizontal',spacing='md',
                            contents=[
                                BoxComponent(layout='vertical',flex=0,
                                    contents=[
                                        TextComponent(text='寶具',weight='bold'),
                                        ImageComponent(url='https://i.imgur.com/4jsuoW8.jpg',align='start',size='xs'),
                                        TextComponent(text='保有技能',weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_302.png',align='start',size='xs'),
                                        TextComponent(text='↓強化後', weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_302.png',align='start',size='xs'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_401.png',margin='xxl',size='xs',align='start'),
                                        TextComponent(text='↓強化後', weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_401.png',size='xs',align='start'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='sm', color='#FFFFFF'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_300.png',margin='xxl',size='xs',align='start'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='職階技能',weight='bold', margin='xxl'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_100.png', size='xs', align='start',),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_102.png', margin='xxl', size='xs', align='start',),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_326.png', margin='xxl', size='xs', align='start',)
                                    ]
                                ),
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='軍神の剣',size='md',color='#FF0000', weight='bold'),
                                        TextComponent(text='對敵全體的強力攻擊400-600%[Lv].',size='xs'),
                                        TextComponent(text='防禦力下降(3回合)[OC]',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='軍略 B',size='xs', weight='bold'),
                                        TextComponent(text='我方全體的寶具威力提升9%-19%',size='xs'),
                                        TextComponent(text='3回合',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='md', color='#FFFFFF'),
                                        TextComponent(text='軍略 B',size='xs', weight='bold'),
                                        TextComponent(text='我方全體的寶具威力提升9%-19%',size='xs'),
                                        TextComponent(text='3回合',size='xs'),
                                        TextComponent(text='敵全體的防禦強化狀態解除',size='xs'),
                                        SeparatorComponent(margin='md', color='#FFFFFF'),
                                        TextComponent(text='天性の肉体 D',size='xs', weight='bold'),
                                        TextComponent(text='自身攻擊弱體耐性提升40-80%',size='xs'),
                                        TextComponent(text='3回合',size='xs'),
                                        TextComponent(text='HP回復1000-2500',size='xs'),
                                        SeparatorComponent(margin='lg', color='#FFFFFF'),
                                        TextComponent(text='天性の肉体 D',size='xs', weight='bold'),
                                        TextComponent(text='自身攻擊弱體耐性提升40-80%',size='xs'),
                                        TextComponent(text='3回合',size='xs'),
                                        TextComponent(text='HP回復1000-2500',size='xs'),
                                        TextComponent(text='星星集中度提升100-300%',size='xs'),
                                        TextComponent(text='→1回合',size='xs'),
                                        SeparatorComponent(margin='xs', color='#FFFFFF'),
                                        TextComponent(text='星の紋章 EX',size='xs', weight='bold'),
                                        TextComponent(text='自身的攻擊力提10%-30%',size='xs'),
                                        TextComponent(text='3回合',size='xs'),
                                        TextComponent(text='星星獲得 5-15',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xl', color='#FFFFFF'),
                                        TextComponent(text='対魔力 B',size='xs', weight='bold'),
                                        TextComponent(text='自身的弱體耐性提升17.5%',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xs', color='#FFFFFF'),
                                        TextComponent(text='騎乗 A',size='xs', weight='bold'),
                                        TextComponent(text='自身的Quick卡性能提升10%',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xs', color='#FFFFFF'),
                                        TextComponent(text='神性 B',size='xs', weight='bold'),
                                        TextComponent(text='對自身賦予傷害加成狀態175',size='xs'),
                                    ]
                                )
                            ]
                        ),
                        footer=BoxComponent(
                            layout='horizontal',
                            contents=[
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        TextComponent(text='技能優先度 :',weight='bold'),
                                        TextComponent(text=' 3 > 2 > 1'),
                                        TextComponent(text='簡評 :', weight='bold',),
                                        #16 char per line
                                    ]
                                )
                             ]
                         )
                 )
                message = FlexSendMessage(alt_text=text, contents=bubble)
                line_bot_api.reply_message(event.reply_token, message)
            #Gilgamesh
            elif text == '3':
                bubble = BubbleContainer(
                        direction='ltr',
                        header=BoxComponent(
                            layout='vertical',
                            contents=[TextComponent(text='吉爾伽美什_ギルガメッシュ(Archer)', align='center')
                            ]
                        ),
                        hero=ImageComponent(url='https://life.tw/upload_file/38/content/5b774356-5863-9842-9659-a0fd2f547bb4.jpg',size='full',margin='md',aspect_ratio='16:9',aspect_mode='cover'),
                        body=BoxComponent(layout='horizontal',spacing='md',
                            contents=[
                                BoxComponent(layout='vertical',flex=0,
                                    contents=[
                                        TextComponent(text='寶具',weight='bold'),
                                        ImageComponent(url='https://i.imgur.com/4jsuoW8.jpg',align='start',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='保有技能',weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_300.png',align='start',size='xs'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_602.png',margin='xxl',size='xs',align='start'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_311.png',margin='xxl',size='xs',align='start'),
                                        TextComponent(text='↓強化後'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_311.png',size='xs', align='start',),
                                        TextComponent(text='職階技能',weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_100.png',size='xs', align='start',),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_101.png',margin='xxl',size='xs', align='start',),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_326.png',margin='xxl',size='xs', align='start',)
                                    ]
                                ),
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='天地乖離す開闢の星',size='xs', weight='bold', color='#FF0000'),
                                        TextComponent(text='寶具威力提升30%(強化後)',size='xs'),
                                        TextComponent(text='全體的強力攻擊400%-600%',size='xs'),
                                        TextComponent(text='┗ 〔Servant〕特攻',size='xs'),
                                        TextComponent(text='┗ 對持有星之力的Servant無效',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='カリスマ A+',size='xs', weight='bold'),
                                        TextComponent(text='全體的攻擊力提升10.5%-21%',size='xs'),
                                        TextComponent(text='3回合',size='xs'),
                                        TextComponent(text='CD 7 ~ 5',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='黄金律 A',size='xs', weight='bold'),
                                        TextComponent(text='NP獲得量提升20%-50%',size='xs'),
                                        TextComponent(text='3回合',size='xs'),
                                        TextComponent(text='CD 8 ~ 6',size='xs'),
                                        SeparatorComponent(margin='lg', color='#FFFFFF'),
                                        TextComponent(text='コレクター EX',size='xs', weight='bold'),
                                        TextComponent(text='星星集中度提升300%-600%',size='xs'),
                                        TextComponent(text='3回合',size='xs'),
                                        TextComponent(text='CD 8 ~ 6',size='xs'),
                                        SeparatorComponent(margin='xl', color='#FFFFFF'),
                                        TextComponent(text='バビロンの蔵 EX',size='xs', weight='bold'),
                                        TextComponent(text='  ┗追加-NP增加20%-30%',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xs', color='#FFFFFF'),
                                        TextComponent(text='対魔力 E',size='xs', weight='bold'),
                                        TextComponent(text='自身的弱體耐性提升10%',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xs', color='#FFFFFF'),
                                        TextComponent(text='単独行動 A+',size='xs', weight='bold'),
                                        TextComponent(text='自身的Critical威力提升11%',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xs', color='#FFFFFF'),
                                        TextComponent(text='神性 B',size='xs', weight='bold'),
                                        TextComponent(text='對自身賦予傷害加成狀態175',size='xs'),
                                    ]
                                )
                            ]
                        ),
                        footer=BoxComponent(
                            layout='horizontal',
                            contents=[
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        TextComponent(text='技能優先度 :',weight='bold'),
                                        TextComponent(text='強化前 : 1 > 2 > 3'),
                                        TextComponent(text='強化後 : 3 > 1 > 2'),
                                        TextComponent(text='簡評 :', weight='bold',),
                                        #16 char per line
                                    ]
                                )
                             ]
                         )
                 )
                message = FlexSendMessage(alt_text=text, contents=bubble)
                line_bot_api.reply_message(event.reply_token, message)
            #Waver Velvet
            elif text == '4':
                bubble = BubbleContainer(
                        direction='ltr',
                        header=BoxComponent(
                            layout='vertical',
                            contents=[TextComponent(text='諸葛孔明〔艾梅洛II世〕', align='center')
                            ]
                        ),
                        hero=ImageComponent(url='https://img1.ali213.net/glpic/2019/04/24/584_2019042455223700.png',size='full',margin='md',aspect_ratio='16:9',aspect_mode='cover'),
                        body=BoxComponent(layout='horizontal',spacing='md',
                            contents=[
                                BoxComponent(layout='vertical',flex=0,
                                    contents=[
                                        TextComponent(text='寶具',weight='bold'),
                                        ImageComponent(url='https://image.spreadshirtmedia.com/image-server/v1/mp/designs/1017286065,width=178,height=178,version=1550290889/fgo-arts-card.png',align='start',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='保有技能',weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_303.png',align='start',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='lg', color='#FFFFFF'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_400.png',margin='xxl',size='xs',align='start'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='sm', color='#FFFFFF'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_300.png',margin='xxl',size='xs',align='start'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='職階技能',weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_104.png',size='xs', align='start',),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_103.png',size='xs', align='start',)
                                    ]
                                ),
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        #np
                                        TextComponent(text='石兵八陣',size='xs', weight='bold', color ='#007AFF'),
                                        TextComponent(text='對敵全體減少一格氣格',size='xs'),
                                        TextComponent(text='機率賦予暈眩狀態(1回合)',size='xs'),
                                        TextComponent(text=' ┗50%-80%[OC]',size='xs'),
                                        TextComponent(text='150%機率賦予詛咒(3回合)',size='xs'),
                                        TextComponent(text='150%機率防禦力下降(3回合)',size='xs'),
                                        TextComponent(text=' ┗10-30%→30-50%(強化後) ',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        #skill 1
                                        TextComponent(text='鑑識眼 A',size='xs', weight='bold'),
                                        TextComponent(text='我方單體爆擊威力提升20-50%',size='xs'),
                                        TextComponent(text=' ┗3回合',size='xs'),
                                        TextComponent(text='我方單體NP增加30%',size='xs'),
                                        TextComponent(text='CD 7 ~ 5',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        #skill 2
                                        TextComponent(text='軍師の忠言 A+',size='xs', weight='bold'),
                                        TextComponent(text='全體防禦力提升20-30%',size='xs'),
                                        TextComponent(text='傷害減免狀態200-500',size='xs'),
                                        TextComponent(text='皆持續3回合',size='xs'),
                                        TextComponent(text='NP增加10%',size='xs'),
                                        TextComponent(text='CD 8 ~ 6',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        #skill 3
                                        TextComponent(text='軍師の指揮 A+',size='xs', weight='bold'),
                                        TextComponent(text='全體的攻擊力提升20-30%',size='xs'),
                                        TextComponent(text='傷害加成狀態',size='xs'),
                                        TextComponent(text='皆持續3回合',size='xs'),
                                        TextComponent(text='NP增加10%',size='xs'),
                                        TextComponent(text='CD 8 ~ 6',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xl', color='#FFFFFF'),
                                        TextComponent(text='陣地作成 A',size='xs', weight='bold'),
                                        TextComponent(text='自身的Arts卡性能提升10%',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xs', color='#FFFFFF'),
                                        TextComponent(text='道具作成 B',size='xs', weight='bold'),
                                        TextComponent(text='自身的弱體賦予成功率提升8%',size='xs'),
                                    ]
                                )
                            ]
                        ),
                        footer=BoxComponent(
                            layout='horizontal',
                            contents=[
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        TextComponent(text='技能優先度 :',weight='bold'),
                                        TextComponent(text='3 > 1 = 2'),
                                        TextComponent(text='簡評 :', weight='bold',),
                                        #16 char per line
                                    ]
                                )
                             ]
                         )
                 )
                message = FlexSendMessage(alt_text=text, contents=bubble)
                line_bot_api.reply_message(event.reply_token, message)
            #Sakata Gintoki
            elif text == '5':
                bubble = BubbleContainer(
                        direction='ltr',
                        header=BoxComponent(
                            layout='vertical',
                            contents=[TextComponent(text='坂田金時', align='center')
                            ]
                        ),
                        hero=ImageComponent(url='https://pbs.twimg.com/media/C1eemqiUcAAcdA8.jpg',size='full',margin='md',aspect_ratio='16:9',aspect_mode='cover'),
                        body=BoxComponent(layout='horizontal',spacing='md',
                            contents=[
                                BoxComponent(layout='vertical',flex=0,
                                    contents=[
                                        TextComponent(text='寶具',weight='bold'),
                                        ImageComponent(url='https://i.imgur.com/4jsuoW8.jpg',align='start',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='保有技能',weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_300.png',align='start',size='xs'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_601.png',margin='xxl',size='xs',align='start'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_401.png',margin='xxl',size='xs',align='start'),
                                        TextComponent(text='職階技能',weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_106.png',size='xs', align='start',),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_326.png',size='xs', align='start',)
                                    ]
                                ),
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        #np
                                        TextComponent(text='黄金衝撃',size='xs', weight='bold', color='#FF0000'),
                                        TextComponent(text='單體超強力攻擊600-1000%',size='xs'),
                                        TextComponent(text='┗無視防禦力提升效果',size='xs'),
                                        TextComponent(text='機率賦予暈眩狀態(1回合)',size='xs'),
                                        TextComponent(text='┗50-100%',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='lg', color='#FFFFFF'),
                                        #skill 1
                                        TextComponent(text='怪力 A+',size='xs', weight='bold'),
                                        TextComponent(text='自身攻擊力提升30-50%',size='xs'),
                                        TextComponent(text='1回合',size='xs'),
                                        TextComponent(text='CD 7 ~ 5',size='xs'),
                                        SeparatorComponent(margin='lg', color='#FFFFFF'),
                                        #skill 2
                                        TextComponent(text='動物会話 C',size='xs', weight='bold'),
                                        TextComponent(text='自身的NP增加30-50%',size='xs'),
                                        TextComponent(text='CD 8 ~ 6',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        #skill 3
                                        TextComponent(text='天性の肉体 A',size='xs', weight='bold'),
                                        TextComponent(text='自身攻擊弱體耐性提升60-120%',size='xs'),
                                        TextComponent(text='HP回復1000-3000',size='xs'),
                                        TextComponent(text='CD 7 ~ 5',size='xs'),
                                        SeparatorComponent(margin='xl', color='#FFFFFF'),
                                        TextComponent(text='狂化 E',size='xs', weight='bold'),
                                        TextComponent(text='Buster卡性能提升2%',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='神性 D',size='xs', weight='bold'),
                                        TextComponent(text='自身賦予傷害加成狀態125',size='xs'),
                                    ]
                                )
                            ]
                        ),
                        footer=BoxComponent(
                            layout='horizontal',
                            contents=[
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        TextComponent(text='技能優先度 :',weight='bold'),
                                        TextComponent(text='2 > 1 > 3'),
                                        TextComponent(text='簡評 :', weight='bold',),
                                        #16 char per line
                                    ]
                                )
                             ]
                         )
                 )
                message = FlexSendMessage(alt_text=text, contents=bubble)
                line_bot_api.reply_message(event.reply_token, message)
            #Vlad III
            elif text == '6':
                bubble = BubbleContainer(
                        direction='ltr',
                        header=BoxComponent(
                            layout='vertical',
                            contents=[TextComponent(text='弗拉德三世', align='center')
                            ]
                        ),
                        hero=ImageComponent(url='https://img.itw01.com/images/2018/03/15/18/2920_XMlYJp_VFZZOEF.jpg',size='full',margin='md',aspect_ratio='16:9',aspect_mode='cover'),
                        body=BoxComponent(layout='horizontal',spacing='md',
                            contents=[
                                BoxComponent(layout='vertical',flex=0,
                                    contents=[
                                        TextComponent(text='寶具',weight='bold'),
                                        ImageComponent(url='https://vignette.wikia.nocookie.net/fategrandorder/images/9/95/Arts.png/revision/latest?cb=20151024070603',align='start',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='保有技能',weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_513.png',align='start',size='xs'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_400.png',margin='xxl',size='xs',align='start'),
                                        TextComponent(text='↓強化後',size='xs'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_328.png',margin='xxl',size='xs',align='start'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_404.png',margin='xxl',size='xs',align='start'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='職階技能',weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_106.png',size='xs', align='start',),
                                    ]
                                ),
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        #np
                                        TextComponent(text='血塗れ王鬼',size='xs', weight='bold', color ='#007AFF'),
                                        TextComponent(text='對單體超強力攻擊600-1000%',size='xs'),
                                        TextComponent(text='┗900-1500%(強化後)',size='xs'),
                                        TextComponent(text='星星獲得15-35[OC]',size='xs'),
                                        TextComponent(text='┗20-40(強化後)',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        #skill 1
                                        TextComponent(text='吸血 A',size='xs', weight='bold'),
                                        TextComponent(text='敵單體氣格機率減少1格(80-100%)',size='xs'),
                                        TextComponent(text='自身NP增加20-30%',size='xs'),
                                        TextComponent(text='CD 8 ~ 6',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        #skill 2
                                        TextComponent(text='変化 C',size='xs', weight='bold'),
                                        TextComponent(text='自身的防禦力提升16-24%',size='xs'),
                                        TextComponent(text='3回合',size='xs'),
                                        TextComponent(text='CD 7 ~ 5',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='鮮血の伝承 A+',size='xs', weight='bold'),
                                        TextComponent(text='自身的防禦力提升20-30%%',size='xs'),
                                        TextComponent(text='┗攻擊力提升20-30%',size='xs'),
                                        TextComponent(text='皆持續3回合',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        #skill 3
                                        TextComponent(text='戦闘続行 A',size='xs', weight='bold'),
                                        TextComponent(text='自身根性狀態1000-2500',size='xs'),
                                        TextComponent(text='1次・5回合',size='xs'),
                                        TextComponent(text='CD 9 ~ 7',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='sm', color='#FFFFFF'),
                                        TextComponent(text='狂化 EX',size='xs', weight='bold'),
                                        TextComponent(text='自身的B卡性能提升12%',size='xs'),
                                    ]
                                )
                            ]
                        ),
                        footer=BoxComponent(
                            layout='horizontal',
                            contents=[
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        TextComponent(text='技能優先度 :',weight='bold'),
                                        TextComponent(text='強化前 : 1 > 2 > 3'),
                                        TextComponent(text='強化後 : 2 > 1 > 3'),
                                        TextComponent(text='簡評 :', weight='bold',),
                                        #16 char per line
                                    ]
                                )
                             ]
                         )
                 )
                message = FlexSendMessage(alt_text=text, contents=bubble)
                line_bot_api.reply_message(event.reply_token, message)
            #Jeanne D'Arc
            elif text == '7':
                bubble = BubbleContainer(
                        direction='ltr',
                        header=BoxComponent(
                            layout='vertical',
                            contents=[TextComponent(text='貞德', align='center')
                            ]
                        ),
                        hero=ImageComponent(url='https://c4.wallpaperflare.com/wallpaper/303/592/917/armor-avamone-azomo-fate-grand-order-wallpaper-preview.jpg',size='full',margin='md',aspect_ratio='16:9',aspect_mode='cover'),
                        body=BoxComponent(layout='horizontal',spacing='md',
                            contents=[
                                BoxComponent(layout='vertical',flex=0,
                                    contents=[
                                        TextComponent(text='寶具',weight='bold'),
                                        ImageComponent(url='https://vignette.wikia.nocookie.net/fategrandorder/images/9/95/Arts.png/revision/latest?cb=20151024070603',align='start',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='lg', color='#FFFFFF'),
                                        TextComponent(text='保有技能',weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_605.png',align='start',size='xs'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_506.png',margin='xxl',size='xs',align='start'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_508.png',margin='xxl',size='xs',align='start'),
                                        TextComponent(text='職階技能',weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_100.png',margin='xxl',size='xs', align='start',),
                                    ]
                                ),
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        #np
                                        TextComponent(text='我が神はここにありて',size='xs', weight='bold',color='#007AFF'),
                                        TextComponent(text='我方全體賦予無敵狀態(1回合)',size='xs'),
                                        TextComponent(text='防禦力提升5-25%(3回合)',size='xs'),
                                        TextComponent(text='每回合HP回復狀態1000-3000',size='xs'),
                                        TextComponent(text='┗2回合',size='xs'),
                                        TextComponent(text='自身賦予暈眩狀態(2回合)',size='xs'),
                                        TextComponent(text='┗弱體狀態解除(強化後)',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        #skill 1
                                        TextComponent(text='啓示 A',size='xs', weight='bold'),
                                        TextComponent(text='每回合星星獲得 3 - 9',size='xs'),
                                        TextComponent(text='3回合',size='xs'),
                                        TextComponent(text='CD 8 ~ 6',size='xs'),
                                        SeparatorComponent(margin='xl', color='#FFFFFF'),
                                        #skill 2
                                        TextComponent(text='真名看破 B',size='xs', weight='bold'),
                                        TextComponent(text='敵單體從者寶具威力下降15-30%',size='xs'),
                                        TextComponent(text='1回合',size='xs'),
                                        TextComponent(text='CD 7 ~ 6',size='xs'),
                                        SeparatorComponent(margin='lg', color='#FFFFFF'),
                                        #skill 3
                                        TextComponent(text='神明裁決 A',size='xs', weight='bold'),
                                        TextComponent(text='機率賦予敵單體從者暈眩70-120%',size='xs'),
                                        TextComponent(text='1回合',size='xs'),
                                        TextComponent(text='CD 8 ~ 6',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='lg', color='#FFFFFF'),
                                        TextComponent(text='対魔力 EX',size='xs', weight='bold'),
                                        TextComponent(text='自身弱體耐性提升25%',size='xs'),
                                    ]
                                )
                            ]
                        ),
                        footer=BoxComponent(
                            layout='horizontal',
                            contents=[
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        TextComponent(text='技能優先度 :',weight='bold'),
                                        TextComponent(text='1 = 2 = 3'),
                                        TextComponent(text='簡評 :', weight='bold',),
                                        #16 char per line
                                    ]
                                )
                             ]
                         )
                 )
                message = FlexSendMessage(alt_text=text, contents=bubble)
                line_bot_api.reply_message(event.reply_token, message)
            #Orion
            elif text == '8':
                bubble = BubbleContainer(
                        direction='ltr',
                        header=BoxComponent(
                            layout='vertical',
                            contents=[TextComponent(text='俄里翁', align='center')
                            ]
                        ),
                        hero=ImageComponent(url='https://i-ogp.pximg.net/c/540x540_70/img-master/img/2015/09/30/21/55/24/52788850_p0_square1200.jpg',size='full',margin='md',aspect_ratio='16:9',aspect_mode='cover'),
                        body=BoxComponent(layout='horizontal',spacing='md',
                            contents=[
                                BoxComponent(layout='vertical',flex=0,
                                    contents=[
                                        TextComponent(text='寶具',weight='bold'),
                                        ImageComponent(url='https://vignette.wikia.nocookie.net/fategrandorder/images/9/95/Arts.png/revision/latest?cb=20151024070603',align='start',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='保有技能',weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_328.png',align='start',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='lg', color='#FFFFFF'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_301.png',margin='xxl',size='xs',align='start'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_402.png',margin='xxl',size='xs',align='start'),
                                        TextComponent(text='職階技能',weight='bold',margin='xxl'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_100.png',size='xs', align='start',),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_101.png',margin='xxl',size='xs', align='start',)
                                    ]
                                ),
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        #np
                                        TextComponent(text='月女神の愛矢恋矢',size='xs', weight='bold', color='#007AFF'),
                                        TextComponent(text='對敵單體強力攻擊900-1500%',size='xs'),
                                        TextComponent(text='┗1200-1800%(強化後)',size='xs'),
                                        TextComponent(text='攻擊力大下降20%(3回合)',size='xs'),
                                        TextComponent(text='NP以機率減少20(60-100%)[OC]',size='xs'),
                                        TextComponent(text='┗100%(強化後)',size='xs'),
                                        TextComponent(text='爆擊發生率下降(3回合)',size='xs'),
                                        TextComponent(text='┗20-60%(強化後)',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        #skill 1
                                        TextComponent(text='女神の寵愛 EX',size='xs', weight='bold'),
                                        TextComponent(text='禦力大提升30-50%(1回合)',size='xs'),
                                        TextComponent(text='攻擊力提升20%(3回合)',size='xs'),
                                        TextComponent(text='弱體耐性提升50%(3回合)',size='xs'),
                                        TextComponent(text='CD 7 ~ 5',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        #skill 2
                                        TextComponent(text='移り気への楔 A+',size='xs', weight='bold'),
                                        TextComponent(text='對自身賦予〔男性〕特攻狀態',size='xs'),
                                        TextComponent(text='┗50-100%(1回合)',size='xs'),
                                        TextComponent(text='CD 7 ~ 5',size='xs'),
                                        SeparatorComponent(margin='xl', color='#FFFFFF'),
                                        #skill 3
                                        TextComponent(text='心眼（偽） B-',size='xs', weight='bold'),
                                        TextComponent(text='對自身賦予迴避狀態(1回合)',size='xs'),
                                        TextComponent(text='爆擊威力提升17-34%(3回合)',size='xs'),
                                        TextComponent(text='CD 8 ~ 6',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='md', color='#FFFFFF'),
                                        TextComponent(text='対魔力 D',size='xs', weight='bold'),
                                        TextComponent(text='自身的弱體耐性提升12.5%',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xs', color='#FFFFFF'),
                                        TextComponent(text='単独行動 A+',size='xs', weight='bold'),
                                        TextComponent(text='自身的爆擊威力提升11%',size='xs'),
                                    ]
                                )
                            ]
                        ),
                        footer=BoxComponent(
                            layout='horizontal',
                            contents=[
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        TextComponent(text='技能優先度 :',weight='bold'),
                                        TextComponent(text='1 > 2 > 3'),
                                        TextComponent(text='簡評 :', weight='bold',),
                                        #16 char per line
                                    ]
                                )
                             ]
                         )
                 )
                message = FlexSendMessage(alt_text=text, contents=bubble)
                line_bot_api.reply_message(event.reply_token, message)
            #Tamamo no mae
            #Drake
            
            #Okita(Saber)
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='查無此從者'))
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue


    return 'OK'


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)
    
    
def nothing():
    """elif text == '2':
                bubble = BubbleContainer(
                        direction='ltr',
                        header=BoxComponent(
                            layout='vertical',
                            contents=[TextComponent(text='阿爾托莉亞Alter (Saber)', align='center')
                            ]
                        ),
                        hero=ImageComponent(url='https://images7.alphacoders.com/986/986869.png',size='full',margin='md',aspect_ratio='16:9',aspect_mode='cover'),
                        body=BoxComponent(layout='horizontal',spacing='md',
                            contents=[
                                BoxComponent(layout='vertical',flex=0,
                                    contents=[
                                        TextComponent(text='寶具', weight='bold'),
                                        ImageComponent(url='https://i.imgur.com/4jsuoW8.jpg',align='start',size='xs'
                                        ),
                                        TextComponent(text='保有技能', weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_306.png',align='start',size='xs'
                                        ),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_603.png',margin='xxl',size='xs',align='start'
                                        ),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_300.png',margin='xxl',size='xs',align='start'
                                        ),
                                        TextComponent(text='職階技能', weight='bold'),
                                        ImageComponent(url='https://kazemai.github.io/fgo-vz/common/images/SkillIcon/SkillIcon_100.png',margin='xxl',size='xs',align='start'
                                        ),
                                    ]
                                ),
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='約束された勝利の剣',size='md', color='#FF0000'),
                                        TextComponent(text='對敵全體攻擊 400%-500%[Lv.]' ,size='xs'),
                                        TextComponent(text='自身NP再累積 20%-50%[Oc]' ,size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),x
                                        TextComponent(text='魔力放出 A',size='xs'),
                                        TextComponent(text='自身的B卡性能提升30% - 50%',size='xs'),
                                        TextComponent(text='1回合',size='xs'),
                                        TextComponent(text='冷卻7 ~ 5回合',size='xs'),
                                        SeparatorComponent(margin='lg', color='#FFFFFF'),
                                        TextComponent(text='直感 B',size='xs'),
                                        TextComponent(text='星星大量獲得 4 - 14',size='xs'),
                                        TextComponent(text='冷卻7 ~ 5回合',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        TextComponent(text='カリスマ E',size='xs'),
                                        TextComponent(text='全體的攻擊力提升 6% - 12%',size='xs'),
                                        TextComponent(text='3回合',size='xs'),
                                        TextComponent(text='冷卻7 ~ 5回合',size='xs'),
                                        SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                        SeparatorComponent(margin='xl', color='#FFFFFF'),
                                        TextComponent(text='対魔力 B', size='xs'),
                                        TextComponent(text='自身的弱體耐性提升17.5%', size='xs'),
                                    ]
                                )
                            ]
                        ),
                        footer=BoxComponent(
                            layout='horizontal',
                            contents=[
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        TextComponent(text='技能優先度 :',weight='bold'),
                                        TextComponent(text='1 = 3 > 2'),
                                        TextComponent(text='簡評 :', weight='bold',),
                                        #16 char per line
                                    ]
                                )
                             ]
                         )
                 )
                message = FlexSendMessage(alt_text=text, contents=bubble)
                line_bot_api.reply_message(event.reply_token, message)"""
