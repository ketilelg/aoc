#!/usr/bin/perl

my $pos=0;
my $depth=0;
my $aim=0;

while(<>)
{
    /(\w+)\s+(\w+)/;
    $com=$1;
    $val=$2;
    if($com =~ /forward/) {$pos+=$val; $depth+=($aim*$val)}
    if($com =~ /down/) {$aim+=$val;}
    if($com =~ /up/) {$aim-=$val;}
print "$com $val $aim pos: $pos depth: $depth\n";
}
$res=$depth*$pos;
print "pos: $pos depth: $depth $res\n";
