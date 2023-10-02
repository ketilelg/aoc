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

my $winner;
my $score=0;

$winner = play(\@hand1,\@hand2);

print "winner: $winner\n";

print "score: $score\n";


sub play
{
    my @hand1=@{$_[0]};
    my @hand2=@{$_[1]};
    
    my $winner=0;
    my $round=1;
    my %prevs; #tidligere runder, som vi kanskje har spilt?
    
    while(!$winner)
    {
	my $thisround= join("-",@hand1).",".join("-",@hand2); #identifiserende streng for runden
	print "$round:\n\np1: @hand1\n";
	print "p2: @hand2\n$thisround\n";
	if($prevs{$thisround})
	{

	    my $mult=1;
	    while (my $v=pop @hand1)
	    {
		$score+=$v*$mult;
		$mult++;
	    }
	    print "repeatscore: $score\n";
	    
	    return 1;
	}
	else
	{
	    $prevs{$thisround}=1;
	}
	



	# draw top cards:
	
	my $p1c=shift @hand1;
	
	my $p2c=shift @hand2;
	
	if (($p1c <= $#hand1+1) && ($p2c<=$#hand2+1))
	{ #recurse!
	    print "recurse, $p1c, $p2c\n";
	    my @h1s=@hand1[0..$p1c-1];
	    my @h2s=@hand2[0..$p2c-1];
	    
	    if (play(\@h1s,\@h2s)==1)
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
	else
	{
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
	print "end round $round:\n\np1: @hand1\n";
	print "p2: @hand2\n\n";
	if ($#hand1<0) { $winner=2; }
	if ($#hand2<0) { $winner=1; }
	
	$round++;
    }

    $score=0;
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
    return $winner;
}
