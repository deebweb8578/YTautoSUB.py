
<?php
/*
ZIHAD HOSSAIN RAFI
*/
// Started //

// Msg Usage //
if ( $argc < 2 ){
  print " __     __      _______    _                    
 \ \   / /     |__   __|  | |                   
  \ \_/ /__  _   _| |_   _| |__   ___           
   \   / _ \| | | | | | | | '_ \ / _ \          
    | | (_) | |_| | | |_| | |_) |  __/          
   _|_|\___/ \__,_|_|\__,_|_.__/ \___|          
  / ____|     | |                 (_) |         
 | (___  _   _| |__  ___  ___ _ __ _| |__   ___ 
  \___ \| | | | '_ \/ __|/ __| '__| | '_ \ / _ \
  ____) | |_| | |_) \__ \ (__| |  | | |_) |  __/
 |_____/ \__,_|_.__/|___/\___|_|  |_|_.__/ \___|
";
  exit( "[??] Youtube Auto Subscribe  [??]\n[??]   ZIHAD HOSSAIN RAFI   [??]\n----------------------------------\nPerintah: php YTautoSUB.php <URL YouToube>\n\n\n" );
}
// Config //
  print " __     __      _______    _                    
 \ \   / /     |__   __|  | |                   
  \ \_/ /__  _   _| |_   _| |__   ___           
   \   / _ \| | | | | | | | '_ \ / _ \          
    | | (_) | |_| | | |_| | |_) |  __/          
   _|_|\___/ \__,_|_|\__,_|_.__/ \___|          
  / ____|     | |                 (_) |         
 | (___  _   _| |__  ___  ___ _ __ _| |__   ___ 
  \___ \| | | | '_ \/ __|/ __| '__| | '_ \ / _ \
  ____) | |_| | |_) \__ \ (__| |  | | |_) |  __/
 |_____/ \__,_|_.__/|___/\___|_|  |_|_.__/ \___|
";
echo "\033[1;37m[\033[1;32m*\033[1;37m] Devoloped by:\033[1;32m NAZMUL TUFAN\n";
echo "\033[1;37m[\033[1;32m+\033[1;37m] Link Channel: \033[1;32m ".$argv[1]."\n";
echo "\033[1;37m[\033[1;32m*\033[1;37m] Auto Subscribe:\033[1;32m Started\n";
echo "\033[1;32m[\033[1;37m~\033[1;32m] Proses Time: \033[1;33m".date("Y/m/d H:i:s")."\n";
echo "\033[1;32m[\033[1;37m@\033[1;32m] Refres Subscribe[\033[1;37m5\033[1;32m]\033[1;37m Seconds\n\n";
while (1){
  $channel = $argv[1];
  $t = file_get_contents($channel);
  $pattern = '/yt-uix-tooltip" title="(.*)" tabindex/';
  preg_match($pattern, $t, $matches, PREG_OFFSET_CAPTURE);
  echo "\033[1;32m[\033[1;37m+\033[1;32m]\033[1;37m Auto >>>\033[1;32m ".$matches[1][0]." \033[1;37m<<< \033[1;32mSubscribe\n";
  for($s=5; $s >=0; $s--){
  echo "Sedang Subscribe... [ ${s}s ] \r";
  sleep(1);
  }
  echo "";
}
?>