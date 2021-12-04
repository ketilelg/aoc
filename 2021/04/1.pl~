#!/usr/bin/perl

my $pos=0;
my $depth=0;

while(<>)
{
    /(\w+)\s+(\w+)/;
    $com=$1;
    $val=$2;
    if($com =~ /forward/) {$pos+=$val;}
    if($com =~ /down/) {$depth+=$val;}
    if($com =~ /up/) {$depth-=$val;}
print "$com $val pos: $pos depth: $depth\n";
}
$res=$depth*$pos;
print "pos: $pos depth: $depth $res\n";
