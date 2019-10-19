#!/usr/bin/env node

const process = require("process");
const path = require("path");
const os = require("os");
const child = require("child_process");
const global_package_path = child.spawnSync( 'npm', [ 'root' , '-g' ] , { encoding: 'utf8' } ).stdout.trim();

process.on( "unhandledRejection" , function( reason , p ) {
	console.error( reason, "Unhandled Rejection at Promise" , p );
	console.trace();
});
process.on( "uncaughtException" , function( err ) {
	console.error( err , "Uncaught Exception thrown" );
	console.trace();
});

const shell = require( path.join( global_package_path ,  "shelljs" ) );

function OS_COMMAND( wTask ) {
	try {
		let result = null;
		let x1 = shell.exec( wTask , { silent: true , async: false } );
		if ( x1.stderr ) { result = x1.stderr }
		else { result = x1.stdout.trim() }
		return( result );
	}
	catch( error ) { console.log( error ); return( error ); }
}
module.exports.os_command = OS_COMMAND;

function GET_DEFUALT_GATEWAY() {
	try {
		let output = child.spawnSync( 'netstat', [ '-r' , '-n' ] , { encoding: 'utf8' } );
		output = output.stdout.trim();
		const lines = output.split( "\n" );
		for ( let i = 0; i < lines.length; ++i ) {
			let items = lines[ i ].split( " " );
			items = items.filter( x => x !== "" );
			for ( let j = 0; j < items.length; ++j ) {
				let item = items[ j ].replace( /\s/g , "" );
				if ( item === "default" ) {
					let default_gateway = items[ j + 1 ];
					default_gateway = default_gateway.replace( /\s/g , "" );
					return default_gateway;
				}
			}
		}
		return false;
	}
	catch( error ) { console.log( error ); return false; }
}

// Google Home Mac Address Masks
// const GOOGLE_MAC_ADDRESS_PREFIXES = [
//     "0c:80:63" , // local testing
//     "00:1a:11" ,
//     "3c:5a:b4" ,
//     "54:60:09" ,
//     "94:eb:2c" ,
//     "a4:77:33" ,
//     "da:a1:19" ,
//     "f4:03:04" ,
//     "f4:f5:d8" , // Google Home ?
//     "f4:f5:e8" ,
//     "f8:8f:ca" ,
// ];

const GOOGLE_MAC_ADDRESS_PREFIXES = [
	//"f4:f5:d8:cc:ad:b0" , // Google Home
	"f4:f5:d8:06:f3:02" , // Google ChromeCast
];

function GET_GOOGLE_MAC_ADDRESS_IPS() {
	try {
		console.log( "Interfaces ==== " );
		const interfaces = Object.keys( os.networkInterfaces() );
		console.log( interfaces );
		let results = [];
		// sudo arp-scan --interface=eth0 --localnet
		for( let j = 0; j < interfaces.length; ++j ) {
			//let output = child.spawnSync( 'sudo arp-scan', [ '-interface=' + interfaces[ j ] , '--localnet' ] , { encoding: 'utf8' } );
			let output = OS_COMMAND( `sudo arp-scan --interface=${ interfaces[ j ] } --localnet` );
			const lines = output.split( "\n" );
			if ( !lines ) { continue; }
			for ( let i = 0; i < lines.length; ++i ) {
				let items = lines[ i ].split( " " );
				if ( !items ) { continue; }
				items = items.map( x=> x.split( "\t" ) );
				for ( let x = 0; x < items.length; ++x ) {
					for ( let y = 0; y < items[ x ].length; ++y ) {
						for ( let z = 0; z < GOOGLE_MAC_ADDRESS_PREFIXES.length; ++z ){
							if ( items[ x ][ y ].indexOf( GOOGLE_MAC_ADDRESS_PREFIXES[ z ] ) !== -1 ) {
								if ( !items[ x ][ 0 ] ) { continue; }
								results.push( items[ x ][ 0 ] );
							}
						}
					}
				}
			}
		}
		return results;
	}
	catch( error ) { console.log( error ); return false; }
}

( async ()=> {

	const google_ips = GET_GOOGLE_MAC_ADDRESS_IPS();
	console.log( google_ips );
	if ( !google_ips ) { return false; }
	const live_twitch_stream_m3u8_url = OS_COMMAND( `youtube-dl 'https://www.twitch.tv/${ process.argv[ 2 ] }' -g` );
	console.log( live_twitch_stream_m3u8_url );
	OS_COMMAND( `castnow --address ${ google_ips[ 0 ] } ${ live_twitch_stream_m3u8_url }` );

})();