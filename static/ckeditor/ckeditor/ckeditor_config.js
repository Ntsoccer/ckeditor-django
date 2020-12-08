CKEDITOR.on('instanceReady', function (ev) {
  const editor = ev.editor;

  editor.on('fileUploadRequest', function (ev) {
    const fileLoader = ev.data.fileLoader;
    // Notificationsをbindすることでメインの編集画面に通知が出るが、今回は別Dialogなのであまり意味がない。
    // CKEDITOR.fileTools.bindNotifications(fileLoader.editor, fileLoader);

    fileLoader.on("uploading", function () {
      console.log("アップロード開始");
    });

    fileLoader.on("uploaded", function () {
      console.log("アップロード完了");
    });

    fileLoader.on("error", function () {
      console.log("アップロードエラー");
    });

    fileLoader.on("abort", function () {
      console.log("アップロード失敗");
    });
  });
});

AWS_QUERYSTRING_AUTH = False

