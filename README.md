# educationTelegramBot
<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="">
    </head>
    <body>

        <!--[if lt IE 7]>
            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="#">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->
        
        <style>

            .function {
                display: block;
                margin-left: auto;
                margin-right: auto 

            }

            .main {
                width:  80%;
                display: block;
                margin-left: auto;
                margin-right: auto 
            }
            .stiled_text{
                padding-left: 10px;
                display: block;
                margin-left: auto;
                margin-right: auto 
            }
            .stiled_header{
                display: block;
                margin-left: auto;
                margin-right: auto 

            }
            .add_directory img{
                display: block;
                margin-left: auto;
                margin-right: auto 
            }

            .text{
                padding-left: 10px;
                padding-right: 10px;
            }
        </style>



        <div class="main">
            <div class="function">
                <h3 class="stiled_header">Main about bot realization</h1>

                <p class="stiled_text">
                    The bot written in Python is built on the basis of the architectural pattern state machine pattern, the main class of the bot is a singleton and implements basic services for working with state parameters. The cataloger in which the manager Linkmanager is currently located acts as a status indicator
                </p>
            </div>
            <div class="about_command_development">
                <p>to develop commands you need to develop routing in the data directory</p>
                <p>for example, in order to make a theme, you need to add a folder to the theme directory</p>
                <p>in addition, you need to add the path for the routing files</p>
                <h4 style="text-align: center;">Example</h4>
                <div class="add_directory">
                    <img src="./documentation/example1-modified.jpg" alt="">
                </div>
                <p>in the main folder there is a subdirectory start and a router file with the following structure</p>
                <div class="add_directory">
                    <img src="./documentation/example2-modified.jpg" alt="">
                </div>
                <div>
                    <p><span><b>is_catalog - </b></span>indicates whether the given route is a directory</p>
                    <p><span><b>is_comand - </b></span>indicates whether route is a command specifier</p>
                    <p><span><b>is_many_answer - </b></span>indicates whether there are multiple response options for the route</p>
                </div>
                <h3>Let's analyze these specifiers using examples
                </h3>
                <div>
                    <h4>is_catalog</h4>
                    <p class="text">if we need to divide some categories, for this we divide them by catalogs and enter the names of the catalogs into the route we need</p>
                    <h3 style="text-align: center;">Example</h3>
                </div>
                <div class="add_directory">
                    <img src="./documentation/example3-modified.jpg" alt="">
                </div>
                <div>
                    <p class="text">
                        If we use <b>is_catalog</b> then we need to specify <i>"name"</i> and statements in English and Ukrainian yes commands that lead to transition to this directory
                    </p>
                    <p>But because of the features of the module that reads the Json routes, you need to specify all the parameters even if they are empty</p>
                    <p>As in this example with <i>"command_name"</i> since this route is not a directory, it is not needed</p>
                    <p>Here is part of the file that specifies the paths for the folders from the previous photo</p>
                </div>
                <div class="add_directory">
                    <img src="./documentation/example4-modified.jpg" alt="">
                </div>
                
                <div>
                    <h4>is_comand</h4>
                    <p class="text">this tag defines that the route is a command and when the manager receives it, it will check the presence of a command defined in the command service by its name defined in this same route</p>
                    <p>If we were talking about <b>is_catalog</b> for which there should not be a parameter <i>"command_name"</i> then for this tag there should be</p>
                    <h3 style="text-align: center;">Example</h3>
                </div>
                <div class="add_directory">
                    <img src="./documentation/example5-modified.jpg" alt="">
                </div>

                <div>
                    <h4>is_many_answer</h4>
                    <p class="text">it is quite simple that indicates that you need to break down what is contained in the answers and choose a random one from these options by default the separator is <b>[]</b></p>
                    <p>in addition, to use this specifier, it is necessary to specify a mandatory parameter <i>"number_of_answer"</i></p>
                    <p>this means that for each route, the routing file must also have this parameter</p>
                    <h3 style="text-align: center;">Example</h3>
                </div>
                <div class="add_directory">
                    <img src="./documentation/example6-modified.jpg" alt="">
                </div>

                <div>
                    <h2>Writing commands</h2>
                    <p class="text">each team implements a strategy and has an internal state</p>
                    <p>each command must have at least 2 methods</p>
                    <div class="text">
                        <div class="text">
                            <i><b>run()</b></i>
                        </div>
                        <div class="text">
                            <i><b>reset()</b></i>
                        </div>
                    </div>
                    <h3>run</h3>
                    <div class="text">
                        a command that, depending on the state, performs operations and gives a response 
                        <h4>response</h4>
                        <div class="text">
                            <p class="text"> response: list [ ansver: str, state: bool ]</p>
                            <div>
                                <h4>ansver</h4> - this is what the user will see after executing this state
                                <h4>state</h4> - this is a status that says whether the command is finished <b>[false]</b> or not <b>[true]</b>
                            </div>
                        </div>
                        <h3 style="text-align: center;">Example</h3>

                        <div class="add_directory">
                            <img src="./documentation/example8-modified.jpg" alt="">
                        </div>
                    </div>

                    <h3>reset</h3>
                    <div class="text">
                        this command updates all the states defined in the command to the base values, including the internal state
                        <h3 style="text-align: center;">Example</h3>
                        
                        <div class="add_directory">
                            <img src="./documentation/example7-modified.jpg" alt="">
                        </div>
                    </div>
                </div>
                <div>
                    <h3>
                        Implementation of the command in the service
                    </h3>
                    <p class="text">in order for the command written by you to work, you need to register it in the command services</p>

                    <h3 style="text-align: center;">Example</h3>
                    <div class="add_directory">
                        <img src="./documentation/example9-modified.jpg" alt="">
                    </div>
                </div>
            </div>

            <div>
                <h2>developed by óchiAnthropos</h2>

            </div>
        </div>
        <script src="" async defer></script>
    </body>
</html>