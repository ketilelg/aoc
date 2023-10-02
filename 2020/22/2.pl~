#!/opt/local/bin/perl

use strict;

$_=<>; #skip "player 1";

my @hands;
my @hand1;
my @hand2;

$_=<>; # les inn første tall
my $i=0;
while (/(\d+)/)
{
    $hand1[$i] = $1;
    $_=<>;
    $i++
}
#er på blank linje. les over neste, repeat:
my $i=0;
$_=<>;
while (<>)
{
    chomp;
    $hand2[$i] = $_;
    $i++;
}

my $winner=0;

while(!$winner)
{
     print "p1: @hand1\n";
    print "p2: @hand2\n\n";

    my $p1c=shift @hand1;
    if ($#hand1<0) { $winner=2; }
    
    my $p2c=shift @hand2;
    if ($#hand2<0) { $winner=1; }

    if ($p1c > $p2c)
    {
	push @hand1,$p1c;
	push @hand1,$p2c;
    }
    else
    {
	push @hand2,$p2c;
	push @hand2,$p1c;
    }
}

print "winner: $winner\n";
     print "p1: @hand1\n";
    print "p2: @hand2\n\n";

my $score=0;
if ($winner==1)
{
    my $mult=1;
    while (my $v=pop @hand1)
    {
	$score+=$v*$mult;
	$mult++;
    }
}
else
{
    my $mult=1;
    while (my $v=pop @hand2)
    {
	$score+=$v*$mult;
	$mult++;
    }
}

print "score: $score\n";
