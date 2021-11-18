let button = document.querySelector("button") ;
button.addEventListener("click",()=>{
    button.disabled=true;
    document.querySelector("body").style.background="pink";
    chrome.tabs.query({currentWindow: true, active: true},
     function(tabs){
        console.log(tabs[0].url);
        let paramString = tabs[0].url.split('?')[1];
        let queryString = new URLSearchParams(paramString);
         const params = Object.fromEntries(queryString.entries());
console.log(params);

document.getElementById("summary").innerHTML= "loading.."
fetch(`http://127.0.0.1:5000/v/${params["v"]}`)
  .then(response => response.text())
  .then(data => {
      console.log(data);
      document.getElementById("summary").innerHTML= data;
    }
  );
        });
        
    }) 

