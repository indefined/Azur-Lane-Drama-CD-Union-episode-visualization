# Azur-Lane-Drama-CD-Union-episode-visualization

A simple visual novel using the Ren'Py engine following the script of the Azur Lane Drama CD.

This project is not a full fledged visual novel. Its main purpose is to mimic the appearance of story cutscenes in Azur Lane.

This branch is base on the [origin](https://github.com/persocom01/Azur-Lane-Drama-CD-Union-episode-visualization) branch, delete story script and add some other Character and image for common use of other part.

## Installation

You need the Ren'Py engine to run this project. Add the project folder to Ren'Py and open it.

## Built With

* [https://www.renpy.org/] - Engine version 7.1.3.
* [https://azurlane.yo-star.com/#/] - Art assets.
* Python 2.7

## Current status

In beta.

Current work:
working on...

## About translate

- Open the project in Ren'py
- Click `Generate Translations`, set the target language name and generate it.
- Edit `screens.rpy`, find `language_picker` part and add a `textbutton` line under it just as the default language, set the `action Language` to target language name.
  -  Set the `text_font` if you need, or delete the `text_font` part if it not necessery.
- Now you can open the game and change language to your translate.
- Open the `tl\{your language}` folder and there may the auto generated translate file on it. Just edit and translate what you want.
  - Add a part like blow to one of the translate rpy file to change your translate font if you need(don't edit the default `gui.rpy` for change your translate font)

```
translate simplified_chinese python:
    gui.system_font = gui.main_font = gui.text_font = gui.name_text_font = gui.interface_text_font = gui.button_text_font = gui.choice_button_text_font = "SourceHanSans-Light-Lite.ttf"
```

## Credits

* [https://github.com/persocom01] - the origin project author.

## License

This project is under MIT License - see [LICENSE.md](LICENSE.md).
Except the images, they are copyright (c) Manjuu Co.,Ltd. & YongShi Co.,Ltd. Contact me to delete if it was overuse to the copyright
