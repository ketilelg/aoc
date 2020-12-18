#!/usr/bin/perl
use strict;

my $sum;

while (<>)
{
    print $_;

    my $s;
    do
    {
	$s=s/(\d+\s\+\s\d+)/eval $1/ge;
#	print "etter eval, $s :  $_\n";
	$s=$s+s/(\([\s\d\*]+\))/eval $1/ge;
#	print "etter eval2, $s : $_\n";
    } while ($s > 0);

    my $res = eval;
    $sum+=$res;
    print "$res\n\n";;

}

print "end: $sum\n";

