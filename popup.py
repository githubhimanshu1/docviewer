import streamlit as st

# D3.js code for a simple bar chart
d3_code = """
<script src="https://d3js.org/d3.v6.min.js"></script>
<button onclick="showModal()">ShowModal</button>
<div id="chart"></div>
<style>
.node {
  cursor: pointer;
}

.node circle {
}

.node text {
  font: 10px sans-serif;
}

.link {
  fill: none;
  stroke: rgb(55, 68, 105);
  stroke-width: 1px;
}
</style>
<script>
    // Your D3.js code goes here
   var treeData = {
  name: "T",
  children: [
    {
      name: "A",
      children: [
        { name: "A1" },
        { name: "A2" },
        { name: "A3" },
        { name: "A4" },
        {
          name: "C",

          children: [
            { name: "C1" },
            {
              name: "D",
              children: [{ name: "D1" }, { name: "D2" }]
            }
          ]
        }
      ]
    },
    { name: "Z" },
    {
      name: "B",
      children: [{ name: "B1" }, { name: "B2" }, { name: "B3" }]
    }
  ]
};

var margin = { top: 20, right: 90, bottom: 30, left: 90 },
  width = 960 - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;
var svg = d3
  .select("#chart")
  .append("svg")
  .attr("width", width + margin.right + margin.left)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var i = 0,
  duration = 750,
  root;
var treemap = d3.tree().size([height, width]);
root = d3.hierarchy(treeData, function(d) {
  return d.children;
});
root.x0 = height / 2;
root.y0 = 0;
root.children.forEach(collapse);

update(root);
function collapse(d) {
  if (d.children) {
    d._children = d.children;
    d._children.forEach(collapse);
    d.children = null;
  }
}

function update(source) {
  var treeData = treemap(root);
  var nodes = treeData.descendants(),
    links = treeData.descendants().slice(1);
  nodes.forEach(function(d) {
    d.y = d.depth * 180;
  });
  var node = svg.selectAll("g.node").data(nodes, function(d) {
    return d.id || (d.id = ++i);
  });
  var nodeEnter = node
    .enter()
    .append("g")
    .attr("class", "node")
    .attr("transform", function(d) {
      return "translate(" + source.y0 + "," + source.x0 + ")";
    })
    .on("click", click);
  nodeEnter
    .attr("class", "node")
    .attr("r", 1e-6)
    .style("fill", function(d) {
      return d.parent ? "rgb(39, 43, 77)" : "#fe6e9e";
    });
  nodeEnter
    .append("rect")
    .attr("rx", function(d) {
      if (d.parent) return d.children || d._children ? 0 : 6;
      return 10;
    })
    .attr("ry", function(d) {
      if (d.parent) return d.children || d._children ? 0 : 6;
      return 10;
    })
    .attr("stroke-width", function(d) {
      return d.parent ? 1 : 0;
    })
    .attr("stroke", function(d) {
      return d.children || d._children
        ? "rgb(3, 192, 220)"
        : "rgb(38, 222, 176)";
    })
    .attr("stroke-dasharray", function(d) {
      return d.children || d._children ? "0" : "2.2";
    })
    .attr("stroke-opacity", function(d) {
      return d.children || d._children ? "1" : "0.6";
    })
    .attr("x", 0)
    .attr("y", -10)
    .attr("width", function(d) {
      return d.parent ? 40 : 20;
    })
    .attr("height", 20);

  nodeEnter
    .append("text")
    .style("fill", function(d) {
      if (d.parent) {
        return d.children || d._children ? "#ffffff" : "rgb(38, 222, 176)";
      }
      return "rgb(39, 43, 77)";
    })
    .attr("dy", ".35em")
    .attr("x", function(d) {
      return d.parent ? 20 : 10;
    })
    .attr("text-anchor", function(d) {
      return "middle";
    })
    .text(function(d) {
      return d.data.name;
    });

  var nodeUpdate = nodeEnter.merge(node);

  nodeUpdate
    .transition()
    .duration(duration)
    .attr("transform", function(d) {
      return "translate(" + d.y + "," + d.x + ")";
    });
  var nodeExit = node
    .exit()
    .transition()
    .duration(duration)
    .attr("transform", function(d) {
      return "translate(" + source.y + "," + source.x + ")";
    })
    .remove();
  nodeExit.select("rect").style("opacity", 1e-6);
  nodeExit.select("rect").attr("stroke-opacity", 1e-6);
  nodeExit.select("text").style("fill-opacity", 1e-6);
  var link = svg.selectAll("path.link").data(links, function(d) {
    return d.id;
  });
  var linkEnter = link
    .enter()
    .insert("path", "g")
    .attr("class", "link")
    .attr("d", function(d) {
      var o = { x: source.x0, y: source.y0 };
      return diagonal(o, o);
    });
  var linkUpdate = linkEnter.merge(link);
  linkUpdate
    .transition()
    .duration(duration)
    .attr("d", function(d) {
      return diagonal(d, d.parent);
    });
  var linkExit = link
    .exit()
    .transition()
    .duration(duration)
    .attr("d", function(d) {
      var o = { x: source.x, y: source.y };
      return diagonal(o, o);
    })
    .remove();
  nodes.forEach(function(d) {
    d.x0 = d.x;
    d.y0 = d.y;
  });
  function diagonal(s, d) {
    path = `M ${s.y} ${s.x}
            C ${(s.y + d.y) / 2} ${s.x},
              ${(s.y + d.y) / 2} ${d.x},
              ${d.y} ${d.x}`;

    return path;
  }
  function click(d) {
    if (d.children) {
      d._children = d.children;
      d.children = null;
    } else {
      d.children = d._children;
      d._children = null;
    }
    update(d);
  }
}


function showModal(){
    var modalRef=window.parent.document.getElementById("modal")
    var chartRef=document.getElementById("chart");
    var clonedChart=chartRef.cloneNode(true)
    clonedChart.style.display="";
    modalRef.appendChild(clonedChart)
    modalRef.showModal();
}


</script>
"""

# Streamlit app content
st.title("D3.js in Streamlit")

# Embed D3.js code using st.components
st.components.v1.html(d3_code, height=800)
st.markdown("""
            <style type="text/css">
            dialog {
            text-align: center;
            background-color: #fff;
            color: #333;
            border: none;
            padding: 30px;
            border-radius: 5px;
            box-shadow: 0 3px 10px 2px rgba(0, 0, 0, 0.5);
            width: 800px;
            max-width: 80%;
            }

            dialog[open] {
            animation: toggle-modal .3s ease-in-out;
            }

            dialog::backdrop {
            background: rgba(0, 0, 0, .5);
            }

            dialog h2 {
            margin: 0 0 30px;
            color: #eee;
            }

            input,
            button {
            padding: 8px 20px;
            margin-bottom: 5px;
            border-radius: 3px;
            border: none;
            cursor: pointer;
            }

            button {
            color: #fff;
            background: #04b95b;
            }

            .close-modal {
            background: #c70000;
            }

            .open-modal { 
            margin-bottom: 40px;
            }

            @keyframes toggle-modal {
            from {
                opacity: 0;
            }

            to {
                opacity: 1;
            }
            }
                       
            .node {
            cursor: pointer;
            }

            .node circle {
            }

            .node text {
            font: 10px sans-serif;
            }

            .link {
            fill: none;
            stroke: rgb(55, 68, 105);
            stroke-width: 1px;
            }

            
            </style>
           
            <dialog id="modal" >Lorem ipsum</dialog>
            """,unsafe_allow_html=True)

# Your remaining Streamlit app content
