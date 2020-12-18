#!/usr/bin/perl
use strict;

my $sum;

while (<>)
{
    do {} while (s/(\d+\s\+\s\d+)/eval $1/ge + s/(\([\s\d\*]+\))/eval $1/ge);

    $sum+=eval;
}

print "end: $sum\n";
