# Keybord-Sound-Maker
キーボードのキーが押されるたびに音を再生し、特定の画像を表示するPythonプログラムです。  
このプログラムは、keyboard、pygame、tkinter、PIL、およびthreadingといったPythonのライブラリを使用しています。  

# 必要なライブラリ
このプログラムを実行するには、以下のPythonライブラリが必要です：
~~~
keyboard  
pygame  
tkinter  
PIL  
threading
~~~

これらのライブラリは、以下のコマンドでインストールできます：
~~~
pip install -r requirements.txt
~~~
注意: tkinterはPythonの標準ライブラリであるため、通常はインストールする必要はありません。

# 使用方法
プログラムと同じディレクトリに、再生したい音声ファイル（'power.mp3'）と表示したい画像ファイル（'kinnikun.jpg'）を配置します。

Pythonでプログラムを実行します：  
任意のキーを押すと、設定した音声が再生されます。  
'esc'キーを押すと、プログラムが終了します。  

# 注意事項
このプログラムは、キーボード入力をグローバルフック（全てのキー入力を監視）しています。そのため、セキュリティソフトウェアによっては、キーロガー（キーストロークを記録するソフトウェア）と誤認される可能性があります。このプログラムはキーストロークを記録したり、送信したりすることはありませんが、その点については自己責任でご使用ください。
