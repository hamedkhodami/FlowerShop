console.log("sdsdsd")
function Setdates(id,title,caption)
{
    $("#id_id").val(id);
    $("#id_title").val(title);
    $("#id_caption").val(caption);
}

function CreateDates()
{
    $("#id_id").val("");
    $("#id_title").val("");
    $("#id_caption").val("0");
}


$(document).ready(function(){
    GetData();
    $("#save-data").click(function(){
    console.log("hello")
        $(".result").show();
        $.ajax({
            type: "POST",
            url:"http://" + window.location.host + "/Ertebat/",
            console.log(" اول خطای ajax". e)
            data:$(".frm").serialize(),
            beforeSend: function(){
                $(".result").html("در حال انجام...");
            } ,
            success: function(result){
                console.log("نتیجه در خواست:",result);
                if(result=="true")
                {
                     $(".result").html("ثبت اطلاعات انجام شد");
                     GetData();

                }
                else if (result=="valid")
                {
                    $(".result").html("خطای اعتبار سنجی : مقدار فیلد ها را به درستی پر کنید");
                }
                else if(result=="exists")
                {
                    $(".result").html(" خطا : اطلاعاتی با این عنوان وجود دارد");
                }
                else
                {
                     $(".result").html(result);
                }
            } ,
            error: function(e) {
                $(".result").html("متاسفانه ثبت اطلاعات انجام نشد");
                console.log(" خطای ajax". e)
            }
        });

    });

    $(".accepted-delete").click(function(){
        $(".result-delete").show();
        $.ajax({
            type: "POST",
            url:"http://" + window.location.host + "/DeleteAsk",
            data:$(".frm-delete").serialize(),
            beforeSend: function(){
                $(".result-delete").html("در حال انجام...");
            } ,
            success: function(result){
                if(result=="true")
                {
                     $(".result-delete").html("حذف اطلاعات انجام شد");
                     GetData();
                }
                else
                {
                     $(".result-delete").html(result);
                }
            } ,
            error: function(e) {
                $(".result-delete").html("متاسفانه حذف اطلاعات انجام نشد");
            }
        })
    });

        $("#Search").on("keyup",function(){
            GetData();
        });
});

function GetData()
{
    $.ajax({
        type: "POST",
        url:"http://" + window.location.host + "/readAsk",
        data:$(".frm-getdata").serialize(),
        beforeSend: function(){
            $(".wite").html("در حال دریافت...");
        } ,
        success: function(result)
            {
                 $(".wite").html("");
                 obj= JSON.parse(result);
                 if(obj.length>0)
                {
                    console.log(obj);
                    trstr="";
                    for(item in obj)
                    {
                        trstr=trstr+"<tr> <td>"+obj[item]["fields"]["title"]+"</td>"+
                        "<td>"+obj[item]["fields"]["caption"]+"</td>"+
                        "<td>"+obj[item]["fields"]["Created"]+"</td>"+
                        "<td>"+
                        "<button type='button' class='btn btn-primary' "+
                        "onclick='Setdates(\""+obj[item]["pk"]+"\",\""+obj[item]["fields"]["title"]+"\",\""+obj[item]["fields"]["caption"]+"\",\""+obj[item]["fields"]["Created"]+"\")'"+
                        "data-toggle='modal' data-target= '#myModal'> ویرایش </button>"
                        +"<button type='button' class='btn btn-danger' "+
                        "onclick=' $(\".id\").val(\""+obj[item]["pk"]+"\"); '"+
                        "data-toggle='modal' data-target= '#myModalDelete'> حذف </button> </td> "
                        +" <tr>";

                    }
                    $(".body-table").html(trstr)
                }
                else
                {
                    $(".wite").html("اطلاعاتی برای نمایش وجود ندارد");
                }
            },
        error: function(e) {
            $(".result").html("متاسفانه حذف اطلاعات انجام نشد");
        }
    })
}

