#!/opt/local/bin/perl
use Switch;
@lines = <>;



chomp $mytime;
chomp $lines[1];
my $prev=0;
my $space="";
my $add=1;

my @input= (split /,/,@lines[1]);

#for my $i (0..($#input-1)) {
    # vi må prøve alle heltallsmultipler av @input[i] til vi finner noe som ,-1, gir %0 mot @input[i-1]..
    # eller noe.
#    if ($input[$i] ne "x") {
#	testthis($i);
#	}
#}

testthis(0,"",1,0);


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
    print "$space tt: $pos\n ";
    if ($pos==$#input) {return 1;}
    my $space=$_[1];
    my $step=$_[2];
    
    my $npos=1;
    my $val=$input[$pos];
    my $prod=$_[3];
    my $unfound=0;
    while ($input[$pos+$npos] eq "x")
    {
	$npos++;
    }
#    print "$space looped over xes. $npos\n";
    my $nval=$input[$pos+$npos];
    print "$space tt preloop $npos $val $nval $step $prod\n";

    while (!$found) {
	my $rem=(($prod+$npos)%$nval);
	print "$space w $mult $val $nval $prod $npos $rem\n";
	if ($rem == 0) {
	    #found a match.. can we use it?
	    $found = testthis($pos+$npos,$space." ",$val,$prod+$npos);
	    if($found) {
		my $starttime= ($prod-$pos);
		print "$space found $starttime $prod $pos\n"; }

	}
	$prod+=$step*$val;
	

    }

    return $found;
    
}
