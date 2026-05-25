from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>

    <title>Air Traffic Control</title>

    <style>

        body{
            margin:0;
            font-family:Arial;
            display:flex;
            justify-content:center;
            align-items:center;
            height:100vh;

            background-image:url('https://images.unsplash.com/photo-1517479149777-5f3b1511d5ad');

            background-size:cover;
            background-position:center;
        }

        .container{

            width:450px;
            padding:30px;
            border-radius:20px;

            background:rgba(255,255,255,0.2);

            backdrop-filter:blur(10px);

            text-align:center;

            color:white;
        }

        input,select,button{

            width:100%;
            padding:12px;
            margin:10px 0;

            border:none;
            border-radius:10px;
        }

        button{

            background:blue;
            color:white;
            font-size:16px;
            cursor:pointer;
        }

        button:hover{

            background:darkblue;
        }

        #message{

            margin-top:15px;
            color:black;
            font-weight:bold;

            background:white;

            padding:10px;

            border-radius:10px;
        }

        #emergency{

            color:red;
            font-weight:bold;
            margin-top:10px;
        }

        #datetime{

            color:white;
        }

    </style>

</head>

<body>

<div class="container">

    <h1>✈ Air Traffic Control</h1>

    <h3 id="datetime"></h3>

    <input type="text"
    id="flight"
    placeholder="Flight Number">

    <input type="text"
    id="airline"
    placeholder="Airline Name">

    <select id="destination">

        <option value="">
        Select Destination
        </option>

        <option value="Delhi">Delhi</option>
        <option value="Mumbai">Mumbai</option>
        <option value="Bangalore">Bangalore</option>
        <option value="Chennai">Chennai</option>
        <option value="Hyderabad">Hyderabad</option>
        <option value="Kolkata">Kolkata</option>
        <option value="Pune">Pune</option>
        <option value="Goa">Goa</option>

    </select>

    <select id="status">

        <option value="">
        Select Status
        </option>

        <option>Landing</option>
        <option>Takeoff</option>
        <option>Delayed</option>
        <option>In Air</option>

    </select>


    <select id="runway">

        <option value="">
        Select Runway
        </option>

        <option>Runway 1</option>
        <option>Runway 2</option>
        <option>Runway 3</option>

    </select>


    <button onclick="checkDetails()">

        Generate Optimized Route

    </button>


    <button onclick="emergencyLanding()">

        Emergency Landing

    </button>


    <p id="message"></p>

    <p id="emergency"></p>

</div>


<script>


function updateDateTime(){

    let now = new Date();

    document.getElementById(
    "datetime").innerHTML =
    now.toLocaleString();
}

setInterval(updateDateTime,1000);

updateDateTime();




// Dijkstra Algorithm

function dijkstra(graph,start,end){

    let distances = {};

    let visited = {};

    let previous = {};



    for(let node in graph){

        distances[node] = Infinity;

        previous[node] = null;
    }

    distances[start] = 0;



    while(true){

        let closestNode = null;


        for(let node in distances){

            if(!visited[node]){

                if(closestNode === null ||

                distances[node] <
                distances[closestNode]){

                    closestNode = node;
                }
            }
        }


        if(closestNode === end){

            break;
        }


        visited[closestNode] = true;



        for(let neighbor in graph[closestNode]){


            let newDistance =

            distances[closestNode] +

            graph[closestNode][neighbor];



            if(newDistance < distances[neighbor]){

                distances[neighbor] = newDistance;

                previous[neighbor] = closestNode;
            }
        }
    }


    let path = [];

    let current = end;



    while(current){

        path.unshift(current);

        current = previous[current];
    }


    return {

        path:path.join(" → "),

        distance:distances[end]
    };
}




function checkDetails(){


    let flight =

    document.getElementById(
    "flight").value;



    let airline =

    document.getElementById(
    "airline").value;



    let destination =

    document.getElementById(
    "destination").value;



    let status =

    document.getElementById(
    "status").value;



    let runway =

    document.getElementById(
    "runway").value;




    if(flight=="" ||

    airline=="" ||

    destination=="" ||

    status=="" ||

    runway==""){


        document.getElementById(
        "message").innerHTML =

        "Please enter all details!";
    }



    else{


        // Different KM for each city

        let cityDistance = {

            "Delhi":1200,
            "Mumbai":980,
            "Bangalore":350,
            "Chennai":500,
            "Hyderabad":650,
            "Kolkata":1500,
            "Pune":720,
            "Goa":450
        };



        let graph = {

            "Airport":{

                "Checkpoint":2,

                "Runway":5
            },



            "Checkpoint":{

                "Runway":2,

                "Tower":4
            },



            "Runway":{

                "Destination":3
            },



            "Tower":{

                "Destination":1
            },



            "Destination":{}
        };



        let result =

        dijkstra(
        graph,
        "Airport",
        "Destination"
        );



        let totalKM = cityDistance[destination];



        let routeType = "";


        if(totalKM <= 700){

            routeType =
            "Shortest Route";
        }

        else{

            routeType =
            "Long Route";
        }



        document.getElementById(
        "message").innerHTML =

        "Optimized Route Generated!<br><br>" +

        "Flight Number: " + flight +

        "<br><br>Airline: " + airline +

        "<br><br>Destination: " + destination +

        "<br><br>Shortest Path: " +

        result.path +

        "<br><br>Total Distance: " +

        totalKM +

        " KM<br><br>" +

        "Route Type: " +

        routeType;
    }
}




function emergencyLanding(){

    document.getElementById(
    "emergency").innerHTML =

    "Emergency Route Assigned Successfully!";
}

</script>

</body>
</html>
"""


@app.route('/')
def home():

    return render_template_string(HTML)



if __name__ == '__main__':

    app.run(debug=True)