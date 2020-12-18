#!/usr/bin/perl
use Switch;
@lines = <>;



chomp $mytime;
chomp $lines[1];
my $prev=0;
my $space="";
my $add=1;
my $final=0;

my @input= (split /,/,@lines[1]);

print "init: antall busser: $#input \n";

#for my $i (0..($#input-1)) {
    # vi må prøve alle heltallsmultipler av @input[i] til vi finner noe som ,-1, gir %0 mot @input[i-1]..
    # eller noe.
#    if ($input[$i] ne "x") {
#	testthis($i);
#	}
#}

testthis(0,"",1,0);

print "end: $final\n";

#for my $bus (split /,/,@lines[1]) {
#    print "$space$bus: $bus ";
#    if ($bus ne "x") {
#	print $bus - ($mytime % $bus);
#    }
#    print "\n";
#    $space.=" ";
#}

sub testthis
{
    # input: posisjon space step start
    # pos hvilken vi undersøker
    # space for utskriftpretty
    # step for hvor store step skal vi ta denne runden (aka + hvor mye)
    # start: hvor starter vi?
    my $mult=1;
    my $pos=$_[0];
    my $space=$_[1];
    print "$space tt: $pos $final\n ";
    if ($pos==$#input)
    {
	$final=$_[3];
	print "$space ttf $final $input[$pos]\n";
	return 1;
    }
    my $step=$_[2];
    
    my $npos=1;
    my $val=$input[$pos];
    #    my $prod=$_[3];
#    my $prod=$final;
    my $unfound=0;
    while ($input[$pos+$npos] eq 'x')
    {
	print "xloop\n";
	$npos++;
    }
#    print "$space looped over xes. $npos\n";
    my $nval=$input[$pos+$npos];
#    print "$space tt preloop $npos $val $nval $step $final\n";

    while (!$found) {
	my $rem=(($final+$npos)%$nval);
	print "$space w $mult $val $nval $final $npos $rem $step\n";
	if ($rem == 0) {
	    #found a match.. can we use it?
	    	    print "$space rem0 $final $npos \n";
	    $final+=$npos;
	    $found = testthis($pos+$npos,$space." ",$val,$final);
	    
	    if($found) {
#		my $starttime= ($final-$pos);
		print "$space found $pos $npos $val $final\n";
		$final-=$npos;
	    }

	}

	
   print "$space loopbot  $final $pos $npos $input[$pos]\n";
	if($found && ($final % $input[$pos]==0))
	{
	    print "$space tilsynelatende match $final $input[$pos]\n";
	    return 1;
	}
	else
	{
	    print "$space nomatch $final $pos $npos $val $final $rem $nval";
	    $found=0;
#	    $final+=($step*$val)*($nval-$rem);
	    $final+=($step*$val);
	    print " $final\n";
	}
    }

    print "$space before return $final $pos $npos\n";

    
}
