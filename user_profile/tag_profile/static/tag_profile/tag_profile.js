
function data_to_table(data,title)
{
	var result = "";
	
	result = result + "<td>" + title + "</td>";
	
	result = result + "<table border='1'><thead><tr><td>标签</td><td>翻译</td><td>权重</td></tr></thead>";
	result = result + "<tbody>";

	for(var i=0 ; i < data.tag_profile.length; i++)
	{
		result = result + "<tr>";
		result = result + "<td>" + data.tag_profile[i].key + "</td>";
		result = result + "<td>" + data.tag_profile[i].translated + "</td>";
		result = result + "<td>" + data.tag_profile[i].value + "</td>";
		result = result + "</tr>";
	}

	result = result + "</tbody></table>";
	
	return result;
}

function tag_search()
{
	var uuid = document.getElementById("uuid").value;

	var url = "tag_search?uuid=" + uuid + "&version=" + "1";

	$.getJSON(url,
		function(data)
		{
			if(data.errno != 0)
			{
				document.getElementById("tag_result").innerHTML = data.result;
			}
			else
			{
				document.getElementById("tag_result").innerHTML = data_to_table(data.result, "资料库①");
			}
		}
	);

	var url = "tag_search?uuid=" + uuid + "&version=" + "2";
	$.getJSON(url,
		function(data2)
		{	
			if(data2.errno!=0)
			{
				document.getElementById("tag_result_2").innerHTML = data2.result;
			}
			else
			{
				document.getElementById("tag_result_2").innerHTML = data_to_table(data2.result, "资料库②");
			}
		}
	);

	return true;
}


