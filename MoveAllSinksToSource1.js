#!/home/morpheous/.nvm/versions/node/v7.4.0/bin/node
require('/home/morpheous/.nvm/versions/node/v7.4.0/lib/node_modules/shelljs/global');
var getInputs = "pacmd list-sink-inputs | awk '/index:/ {print $0};'";
var wInputs = exec( getInputs , { silent:true , async: false }).stdout;
wInputs = wInputs.split("\n");
for ( var i = 0; i < wInputs.length; ++i ) {
	var x1 = wInputs[i].replace(/\s/g, "");
	if ( x1.length == 0 ) { continue; }
	var x2 = x1.split(":");
	if ( !x2 ) { continue; }
	if ( x2.length == 2 && x2[0] === 'index' ) {
		var wExec = "pacmd move-sink-input " + x2[1] + " 1";
		exec( wExec , { silent:true , async: false } );
	}
}
process.exit(1);