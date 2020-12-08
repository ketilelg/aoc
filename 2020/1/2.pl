#!/opt/local/bin/perl

@lines = <>;

# :3
# print @lines;

for $i ( 0 .. $#lines ) {
   for $j ( ($i + 1) .. $#lines ){
   for $k ( ($j + 1) .. $#lines ){

#my $a=chop($lines[$i]);
#my $b=chop($lines[$j]);
#my $c=
      my $su = $lines[$i] + $lines[$j] + $lines[$k]; 

# print "$lines[$i] $lines[$j] $lines[$k] sum: $su\n";
      if ( $su == 2020 ) { print "found it:  $lines[$i] $lines[$j] $lines[$k]"; }
}
}
}

