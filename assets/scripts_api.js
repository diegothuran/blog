function getRandomColor() {
	var letters = '0123456789ABCDEF'.split('');
	var color = '#';
	for (var i = 0; i < 6; i++ ) {
	    color += letters[Math.floor(Math.random() * 16)];
	}
return color;
}

var articles_list = document.getElementById("articles_list");
var chartContainer = document.getElementById("chartContainer");

function posts(){
	articles_list.style.display = "block";
	chartContainer.style.display = "none";
}

////Get the container element
//var container = document.getElementById("sidebar-category");
//
//// Get all buttons with class="btn" inside the container
//var links = container.getElementsByClassName("nav-link");
//
////Loop through the buttons and add the active class to the current/clicked button
//for (var i = 0; i < links.length; i++) {
//	links[i].addEventListener("click", function() {
//    var current = document.getElementsByClassName("active");
//
//    // If there's no active class
//    if (current.length > 0) { 
//      current[0].className = current[0].className.replace(" active", "");
//    }
//
//    // Add the active class to the current/clicked button
//    this.className += " active";
//  });
//}

function myCanvas2(labels_category_timeline, data_category_timeline){
	articles_list.style.display = "none";
	chartContainer.style.display = "block";
	
	document.getElementById("chartContainer").innerHTML = '&nbsp;';
	document.getElementById("chartContainer").innerHTML = '<canvas id="myCanvas" width="600" height="600"></canvas>';
	var ctx = document.getElementById("myCanvas").getContext("2d");
	
    var category_timeline = new Chart(ctx, {
    	type: 'line',
//    	type: 'bar',
        data: {
            labels: labels_category_timeline,
            datasets: [{
//                label: 'Timeline',
                data: data_category_timeline,
//                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    },  
                    scaleLabel: {
                		display: true,
                		labelString: 'Quantidade',
                		fontSize: 14,
                		fontStyle: 'bold'
                			
	                }
                }],
                
                xAxes: [{
                	scaleLabel: {
                		display: true,
                		labelString: 'Data',
                		fontSize: 14,
                		fontStyle: 'bold'
                			
	                }
                }]
            },
        
	        title: {
	            display: true,
	            text: 'Timeline das notícias relacionadas a categoria: Osmar Terra.',
	            fontSize: 16
	        },
	        
	        legend: {
	            display: false
	        },
	        
	        tooltips: {
	            callbacks: {
	                label: function(tooltipItem) {
	                    return Number(tooltipItem.yLabel) + " notícia(s) obtida(s) na data " + tooltipItem.xLabel + " contêm a categoria Osmar Terra"
	                }
	            }
	        }
        }
    });
}

function myCanvas3(labels_category_relation, data_category_relation){
	articles_list.style.display = "none";
	chartContainer.style.display = "block";
	
	document.getElementById("chartContainer").innerHTML = '&nbsp;';
	document.getElementById("chartContainer").innerHTML = '<canvas id="myCanvas" width="600" height="600"></canvas>';
	var ctx = document.getElementById("myCanvas").getContext("2d");
	
	var randomColors = [];
	for (var i in labels_category_relation) {
		randomColors.push(getRandomColor());
	}
    
//    var ctx = document.getElementById("category_relation");
    var category_relation = new Chart(ctx, {
    	//type: 'line',
    	type: 'horizontalBar',
        data: {
            labels: labels_category_relation,
            datasets: [{
//                label: 'Relacionamento entre categorias (Porcentagem de noticias que contem a categoria Osmar Terra e a categoria relacionada)',
                data: data_category_relation,
//                borderWidth: 1
                backgroundColor: randomColors
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    },
                    scaleLabel: {
                		display: true,
                		labelString: 'Categoria',
                		fontSize: 14,
                		fontStyle: 'bold'
                			
	                }
                }],
                
                xAxes: [{
                	scaleLabel: {
                		display: true,
                		labelString: 'Porcentagem (%)',
                		fontSize: 14,
                		fontStyle: 'bold'
                			
	                }
                }]
            },
            
            title: {
                display: true,
                text: 'Relacionamento entre categorias considerando a categoria base: Osmar Terra.',
                fontSize: 16
            },
            
            legend: {
                display: false
            },
            
            tooltips: {
                callbacks: {
                    label: function(tooltipItem) {
                        return Number(tooltipItem.xLabel) + "% das notícias que contêm a categoria " + "Osmar Terra" + " também contêm a categoria " 
                        + tooltipItem.yLabel
                    }
                }
            }
        }
    });
}


function myCanvas4(labels_category_sites, data_category_sites){
	articles_list.style.display = "none";
	chartContainer.style.display = "block";
	
	document.getElementById("chartContainer").innerHTML = '&nbsp;';
	document.getElementById("chartContainer").innerHTML = '<canvas id="myCanvas" width="500" height="1500"></canvas>';
	var ctx = document.getElementById("myCanvas").getContext("2d");
	
    var randomColors = [];
	for (var i in labels_category_sites) {
		randomColors.push(getRandomColor());
	}
	
    var category_sites = new Chart(ctx, {
    	//type: 'line',
    	type: 'horizontalBar',
        data: {
            labels: labels_category_sites,
            datasets: [{
//                label: 'Quantidade de noticias relacionadas a categoria Osmar Terra obtidas do site',
                data: data_category_sites,
                backgroundColor: randomColors
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    },
                    scaleLabel: {
                		display: true,
                		labelString: 'Fonte de informação',
                		fontSize: 14,
                		fontStyle: 'bold'
                			
	                }
                }],
                
                xAxes: [{
                	scaleLabel: {
                		display: true,
                		labelString: 'Quantidade',
                		fontSize: 14,
                		fontStyle: 'bold'
                			
	                }
                }]
            },
            
            title: {
                display: true,
                text: 'Segmentação das fontes de informação considerando a categoria: Osmar Terra.',
                fontSize: 16
            },
            
            legend: {
                display: false
            },
            
            tooltips: {
                callbacks: {
                    label: function(tooltipItem) {
                        return Number(tooltipItem.xLabel) + " notícias que contêm a categoria " + "Osmar Terra" + " foram obtidas do site " 
                        + tooltipItem.yLabel
                    }
                }
            }
            
        }
    });
}

function myCanvas5(word_cloud){
	articles_list.style.display = "none";
	chartContainer.style.display = "block";
	
	document.getElementById("chartContainer").innerHTML = '&nbsp;';
	document.getElementById("chartContainer").innerHTML = '<canvas id="myCanvas" width="600" height="600"></canvas>';
	var ctx = document.getElementById("myCanvas").getContext("2d");
	
	

    	list = [];
    	for (var i in word_cloud) {
    	  list.push([word_cloud[i]["word"], word_cloud[i]["freq"]])
    	}

//    	WordCloud.minFontSize = "15px"
    	WordCloud.minFontSize = "25px"
//		var ctx = document.getElementById("myChart").getContext('2d');
//    	ctx.clearRect(0, 0, ctx.width, ctx.height);
    	WordCloud(document.getElementById('myCanvas'), { list: list} );
}

