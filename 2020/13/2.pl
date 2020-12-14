#!/usr/bin/perl
use Switch;
@lines = <>;

chomp $mytime;
chomp $lines[1];

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
