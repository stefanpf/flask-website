$(function(){
            $('#fileupload').fileupload({
                url: $SCRIPT_ROOT + '/upload',
                dataType: 'json',
                add: function (e, data) {
                  data.submit();
                },
                success:function(response,status) {
                  console.log(response.filename);
                  var filePath = $SCRIPT_ROOT + '/static/media/img/' + response.filename;
                  $('#imgUpload').attr('src',filePath);
                  $('#filePath').val(filePath);
                  console.log('success');
                },
                error:function(error){
                        console.log(error);
                }
            });
      })

$(function() {
  $("#add-project-structure").click(function() {
    $("#post-input-textarea").load($SCRIPT_ROOT + "/static/js/project-structure.txt");
  });
})

$(function() {
  $("#add-blogpost-structure").click(function() {
    $("#post-input-textarea").load($SCRIPT_ROOT + "/static/js/blog-structure.txt");
  });
})
