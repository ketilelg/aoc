#!/usr/bin/perl
use List::Util qw(first max maxstr min minstr reduce shuffle sum);

@crabs=split(",", <>);

my $shortest=100000000;

for my $c (min(@crabs)..max(@crabs))
{
    my $sd=0;
    foreach my $cc (@crabs)
    {
	#finn sumavstand
	$dist=abs($cc-$c);
	    $cost=($dist*($dist+1))/2;
	    $sd+=$cost;
    }
    if ($shortest>$sd) {$shortest=$sd;}
}
print "shortest: $shortest\n";
