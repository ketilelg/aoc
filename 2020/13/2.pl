#!/usr/bin/perl
use Switch;
@lines = <>;



chomp $mytime;
chomp $lines[1];
my $prev=0;
my $space="";
my $add=1;
my $final=0;
my $time=0;
my $factor=1;
my @input= (split /,/,@lines[1]);

my $lastbus=$#input;
print "init: antall busser: $lastbus \n";

while(!$found)
{
    #outer loop: vi iterer fra bunn, med $step som økende variabel.
    my $factor=1;
    my $nx=1;
    for my $i (1..($lastbus))
    {

	# inner loop: iterer over $input til det ikke passer. ta vare på stepverdien..
	print "il: i $i input:i $input[$i] nx $nx";
	if ($input[$i] eq 'x')
	{
	    print " inpx \n";
	    $nx++;
	    next;
	}
	else
	{
	    print " e time $time i $i nx $nx input:i $input[$i] ";
	    $rem=($time+$i) % $input[$i] ;
	    if ($rem == 0 )
	    {
		print "jepp\n";
		$factor*=$input[$i-$nx];
		$found = ($i==$lastbus); 
		$nx=1;
	    }
	    else
	    {
		print " $rem nope\n";
		$time+=($input[$i-$nx]*$factor);
		$nx=1;
		last;
	    }
	    
	}
    }
    print "endloop: $time $factor\n";
}


    # vi må prøve alle heltallsmultipler av @input[i] til vi finner noe som ,-1, gir %0 mot @input[i-1]..
    # eller noe.
#    if ($input[$i] ne "x") {
#	testthis($i);
#	}
#}


print "end: $time\n";

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
	if($final % $input[$pos] == 0)
	{
	    return 1;
	}
	else
	{
	    return 0;
	}
    }
    my $step=$_[2];
    
    my $npos=1;
    my $val=$input[$pos];
    my $found=0;

    while ($input[$pos+$npos] eq 'x')
    {
	print "xloop\n";
	$npos++;
    }
#    print "$space looped over xes. $npos\n";
    my $nval=$input[$pos+$npos];
#    print "$space tt preloop $npos $val $nval $step $final\n";

    my $rem=(($final+$npos)%$nval);
    $final=$val*(($val + 1) % $nval);
	print "$space ttt $mult $val $nval $final $npos $rem $nt $step\n";
        

	    $final+=$npos;
	    $found = testthis($pos+$npos,$space." ",$val,$final);
	    


    print "$space before return $final $pos $npos $found\n";

    
}
