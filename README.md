# FileRenameSerialNumber
指定フォルダ内のファイルを一括で連番リネームする

## 使用するパラメータ
```
dirPath : 対象のディレクトリのパス

fileName : 連番前のファイル名(「xxx連番.拡張子」の「xxx」部分)

sortType : ctime -> ファイルの作成順に連番をつける
         : name  -> リネーム前のファイル名の順番に連番をつける
         ※両方とも「昇順」
```
　
## 使い方１：YAMLファイルにパラメータを記述し実行する方法
「parameters.yml」内にある上記のパラメータを変更  
↓  
「FileRenameSerialNumberByYAMLParams.bat」を実行  
    
## 使い方２：コマンドプロンプトからパラメータを指定して実行する方法
「FileRenameSerialNumber.bat」を実行すると各パラメータの入力を求められるので入力する。
