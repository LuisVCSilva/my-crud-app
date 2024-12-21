var Terminal = Terminal || function(cmdLineContainer, outputContainer) {
  var cmdLine = document.querySelector(cmdLineContainer);
  var output = document.querySelector(outputContainer);

  var requestHandler = null;
  var fs = null;
  var cwd = null;
  var history = [];
  var histpos = 0;
  var histtemp = 0;
  window.addEventListener('click', function(e) {
    cmdLine.focus();
  }, false);

  cmdLine.addEventListener('click', inputTextClick, false);
  cmdLine.addEventListener('keydown', historyHandler, false);
  cmdLine.addEventListener('keydown', processNewCommand, false);

  // Helper functions
  function inputTextClick(e) {
    this.value = this.value;
  }

  function historyHandler(e) {
    if (history.length) {
      if (e.keyCode == 38 || e.keyCode == 40) {
        if (history[histpos]) {
          history[histpos] = this.value;
        } else {
          histtemp = this.value;
        }
      }

      if (e.keyCode == 38) { // up
        histpos--;
        if (histpos < 0) {
          histpos = 0;
        }
      } else if (e.keyCode == 40) { // down
        histpos++;
        if (histpos > history.length) {
          histpos = history.length;
        }
      }

      if (e.keyCode == 38 || e.keyCode == 40) {
        this.value = history[histpos] ? history[histpos] : histtemp;
        this.value = this.value; // Sets cursor to end of input.
      }
    }
  }

  function processNewCommand(e) {
    if(requestHandler==null)
    {
    if (e.keyCode == 9) { // tab
      e.preventDefault();
      // Implement tab suggest.
    } else if (e.keyCode == 13) { // enter
      // Save shell history.
      if (this.value) {
        history[history.length] = this.value;
        histpos = history.length;
      }

      // Duplicate current input and append to output section.
      var line = this.parentNode.parentNode.cloneNode(true);
      line.removeAttribute('id')
      line.classList.add('line');
      var input = line.querySelector('input.cmdline');
      input.autofocus = false;
      input.readOnly = true;
      output.appendChild(line);      
      var cmd = this.value.trim().toLowerCase();
      this.value = '';
      if(cmd!="")
      {
         $.when(requestCommand(cmd)).done(function(a1) {
         input.autofocus = true;
         // Duplicate current input and append to output section.
         //var argString = this.value.replace(cmd, "").trim();
         });
      }
    }
    }
   }

  //
  function output_(html) {
    if (html === undefined) return;
    output.insertAdjacentHTML('beforeEnd', html);
  }

  // Cross-browser impl to get document's height.
  function getDocHeight() {
    var d = document;
    return Math.max(
        Math.max(d.body.scrollHeight, d.documentElement.scrollHeight),
        Math.max(d.body.offsetHeight, d.documentElement.offsetHeight),
        Math.max(d.body.clientHeight, d.documentElement.clientHeight)
      );
    }

  // add custom attributes here. Refer to "this.<custom-attribute>" later via term.<custom-attribute>
  this.user = "guest";
  this.prompt = "free_version";
  this.loggedIn = 0; // no. 1 is admin


   function requestCommand (command) {
   command = encodeURIComponent(command);
   if(command=="clear")
   {
   output.innerHTML = "";
   loadBanner();
   }
   else
   {
   _url = 'evaluate?call='+command;//+"&"+_url.join("&");
   requestHandler = $.ajax({
      url: _url,
      beforeSend: function () { 
         ShowLoadingScreen(); 
      }, // <Show OverLay      
      type: 'GET',
      dataType: 'json',
      success: function (response) {
         if (response=={"error":"timeout"}) {
         output_("<p>Request failed: Server decided that it took too long and aborted it</p>");
         }         
         else {
         //output_(JSON.stringify(response,null,4).replace(/\"/g, "").replace(/\{/g, "").replace(/\}/g, ""));
         /*jQuery.each(response, function(i, val) {
           output_("<h5>" + i + "</h5>");
           output_(val);
         }); */
         /*var btn = document.createElement('div');
         btn.setAttribute("id", "tree");
         output.appendChild(btn);
         console.log(jsonTreeViewer);
         jsonTreeViewer.parse(response);*/
         
         // Get DOM-element for inserting json-tree
         console.log(response["url"]);
         if(response.hasOwnProperty("url")) {
            requestitoHandlino = $.ajax({
               url: response["url"],
               beforeSend: function () { 
                  ShowLoadingScreen(); 
               }, // <Show OverLay      
               type: 'GET',
               dataType: 'json',
               success: function (responsito) {
               response = responsito;
               printResult(response, output);
                   $.toast({
                   heading: 'Computation finished!',
                   text: 'You still have 300 seconds of computation time remaining',
                   bgColor: '#0e8700',
                   allowToastClose: true,    
                   textColor: 'white'
               });               
               }
               }).fail(function (jqXHR, textStatus, error) {
                  FailCase(jqXHR, textStatus, error);
               });
         }
         else
         {
         printResult(response, output);                  
         }         
         }
      },
      complete: function () {
         HideLoadingScreen();
         requestHandler = null;       
         this.value = ''; // Clear/setup line for next input.      
         HideLoadingScreen();
         window.scrollTo(0, getDocHeight());
      } 
   }).fail(function (jqXHR, textStatus, error) {
         FailCase(jqXHR, textStatus, error);
   });
   }
   }
    
   function printResult (response,output) {
      var wrapper = output;
      var data = '';
      try {
         var data = response;
      } catch (e) {}
      var tree = jsonTree.create(data, wrapper);   
   }    
      
   function FailCase (jqXHR, textStatus, error) {
       console.log([jqXHR, textStatus, error]);
       switch(textStatus){
       case "error":
          if (error=="INTERNAL SERVER ERROR") {
          output_("<p>The server could not understand your input</p>");
                $.toast({
                heading: 'Computation failed!',
                text: 'The server wasn\'t able to make sense of your input',
                bgColor: '#870000',
                allowToastClose: true,    
                textColor: 'white'
            });          
          }
          else {
          if(error=="BAD REQUEST")
          {
             output_("<p>Could not complete request: Something wen't wrong in the server</p>");
                   $.toast({
                   heading: 'Computation failed!',
                   text: 'We got a HTTP 400 error, something wen\'t wrong in the server',
                   bgColor: '#870000',
                   allowToastClose: true,    
                   textColor: 'white'
               });          
          }
          else
          {
             output_("<p>Could not complete request: Internet connection error</p>");
                   $.toast({
                   heading: 'Computation failed!',
                   text: 'Server wasn\'t reached, check your Internet connection',
                   bgColor: '#870000',
                   allowToastClose: true,    
                   textColor: 'white'
               });
            }      
         }   
          break;
       case "abort":
          output_("<p>Could not complete request: Aborted by user</p>");
                $.toast({
                heading: 'Computation aborted!',
                text: 'You still have 300 seconds of computation time remaining',
                bgColor: '#fff70d',
                allowToastClose: true,    
                textColor: 'black'
            });             
          break;
       default:
          output_("<p>Request failed:" + textStatus + "</p>");
                $.toast({
                heading: 'Computation failed!',
                text: 'Something wen\'t wrong: ' + textStatus,
                bgColor: '#780000',
                allowToastClose: true,    
                textColor: 'white'
            });          
       }
         this.value = ''; // Clear/setup line for next input.      
         HideLoadingScreen();         
         window.scrollTo(0, getDocHeight());          
   }
   
   function ShowLoadingScreen () {
   var customElement = $("<div>", {
    "class" : "btn btn-danger btn-lg",
    "text"  : "Abort",
    "onclick": "document.getElementById('abortion_site').click();"
   });

      $.LoadingOverlay("show", {
       image       : "/static/loading.gif",
       background              : "rgba(238, 238, 238, 1.0)",
       imageAnimation          : "none",
       imageAutoResize         : true,
       imageResizeFactor       : 2,
       text        : "Loading...",
       custom      : customElement
       });
   }
      
   function HideLoadingScreen () {
     $.LoadingOverlay("hide");     
   }   

  this.abortAjax = () => {
     requestHandler.abort();
  }
   
  this.init = () => {
   var jQueryScript = document.createElement('script');  
   jQueryScript.setAttribute('src','/static/loadingoverlay.js');
   document.head.appendChild(jQueryScript);
   cmdLine.disabled = false;
   loadBanner();   
   $('.prompt').html(this.prompt + "@" + this.user);
  }

  function loadBanner () {
    output_('<p><h2 style="letter-spacing: 4px">Luis\' Terminal</h2></p><p>Request computation by command and thou shall get your computation result by demand</p><p>Type \'help\' for help</p><p>(wow, such hints)</p>');
  }  
  }
