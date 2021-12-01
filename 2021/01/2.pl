#!/usr/bin/perl

@lines = <>;

# print @lines;

$pf=$lines[0];
$psum=$lines[0] + $lines[1] + $lines[2];


for $i ( 3 .. $#lines ) {

    print "$psum\n";
    $sum=$psum-$pf+$lines[$i];
    $pf=$lines[$i-2];
    if($sum>$psum){$incs++;}
    $psum=$sum;

}

print $incs;


