function open_js(){
    var type;
    var file= document.getElementById("myfile").value;
    file= file.replace(/^.*[\\\/]/, '');
    // swal(csv);
    // swal(file);
    var weight;

    if(document.getElementById("tsv").checked == true)
    {   
         type="\t";
         
    }
    if(document.getElementById("csv").checked == true)
    {   
         type=",";
         
    }
    if(document.getElementById("space").checked == true)
    {   
         type=" ";    
    }

    if(document.getElementById("weight1").checked == true)
    {   
         weight=document.getElementById("weight1").value;
         
    }
    if(document.getElementById("weight2").checked == true)
    {
        weight=document.getElementById("weight2").value;
    }

  console.log(file+type+weight)
    
   
    eel.open(file,type,weight)
}


function pic_js(){
    var yes= document.getElementById("graph_yes").value;
    swal("Please be Patient! the graph is in process...");
    eel.pic()
}

eel.expose(pic_return)
function pic_return(x){   
    swal(x);
      
    $("#graph_image").replaceWith('<div id="graph_image"><img class ="card" src="'+x+'">'+ "<br /></div>")

   // document.getElementById("graph_image").innerHTML += '<img class ="card" src="'+x+'">'+ "<br />";

}

function pic_js1(){
    
    var no= document.getElementById("graph_no").value;
    
    swal("Are you sure you don't want to print the graph");
}

function select_function_js(){
    var degree,closeness,betweeness,pagerank;
    var value=["x","x","x","x"];
    if (document.getElementById('degree').checked) {
        degree = document.getElementById("degree").value;
        
    } else {
        degree="";
    }

    if (document.getElementById('betweeness').checked) {
        betweeness = document.getElementById("betweeness").value;
        
    } else {
        betweeness="";
    }

    if (document.getElementById('closeness').checked) {
        closeness = document.getElementById("closeness").value;
        
    } else {
        closeness="";
    }

    if (document.getElementById('pagerank').checked) {
        pagerank = document.getElementById("pagerank").value;
        
    } else {
        pagerank="";
    }

    swal("Please be Patient! the process is on going...")

    value[0]=degree;
    value[1]=pagerank;
    value[2]=betweeness;
    value[3]=closeness;
    eel.method(value);
    
}
eel.expose(select_function_return)
function select_function_return(s){
    swal(s)
}

function top_seed_nodes_js(){
    var val= document.getElementById("topSeedNodes_value").value;
 
    if(val== "" || val==0||val<0)
        swal("value not allowed");
    else{
        eel.top_seed_node(val);
            //document.getElementById("h1").style.display = "block";
        }
}
eel.expose(top_seed_nodes_return)
function top_seed_nodes_return(s){
    document.getElementById("top").innerHTML += s+ "<br />";

}

function affected_nodes_values_js(){
    
    var val= document.getElementById("affected_node").value;
    if(val== "" || val==0||val<0)
        swal("value not allowed");
        else{
            eel.affected_nodes_value(val);
            //document.getElementById("h2").style.display = "block";
        }
}

eel.expose(affected_nodes_values_return)
function affected_nodes_values_return(s){
    document.getElementById("affected").innerHTML += s[0]+ "<br />";
    document.getElementById("affected").innerHTML += s[1]+ "<br />";

}

function affected_nodes_percentage_js(){
    var val= document.getElementById("affected_percentage").value;
    if(val== "" || val==0||val<0)
        swal("value not allowed");
        else{
            eel.affected_node_percentage(val)
            document.getElementById("h3").style.display = "block";
        }
}
eel.expose(affected_nodes_percentage_return)
function affected_nodes_percentage_return(s){
    document.getElementById("percentage").innerHTML += s[0]+ "<br />";
    document.getElementById("percentage").innerHTML += s[1]+ "<br />";
    document.getElementById("percentage").innerHTML += s[2]+ "<br />";
    document.getElementById("percentage").innerHTML += s[3]+ "<br />";
    document.getElementById("percentage").innerHTML += s[4]+ "<br />";
    document.getElementById("percentage").innerHTML += s[5]+ "<br />";
    document.getElementById("percentage").innerHTML += '<img   src="'+s[6]+'">'+ "<br />";

}