#!/usr/bin/perl
use Switch;
@lines = <>;

chomp $mytime;
chomp $lines[1];

my $factor=1; # 
my @input= (split /,/,@lines[1]);
my $time=$input[0]; # dette er tenkt starttid for første buss

my $lastbus=$#input;
print "init: antall busser: $lastbus \n";

while(!$found)
{
    #outer loop: vi iterer over bussene, start med den første..
#     my $factor=$input[0];
    my $factor=1;
    my $nx=1;
    for my $i (1..($lastbus))
    {
	# inner loop: iterer over $input til det ikke passer. ta vare på stepverdien..
#	print "il: i $i input:i $input[$i] nx $nx factor $factor";
	if ($input[$i] eq 'x')
	{
#	    print " inpx \n";
	    $nx++;
	    next;
	}
	else
	{
#	    print " e time $time i $i nx $nx input:i $input[$i] ";
	    $rem=($time+$i) % $input[$i] ;
	    # er vi fremdeles på sporet av en løsning?
	    if ($rem == 0 )
	    {
		# ja. 
#		print "jepp\n";
		$factor*=$input[$i-$nx];
		$found = ($i==$lastbus); 
		$nx=1;
	    }
	    else
	    {
		# nei, det gikk ikke. tilbake til start.
#		print " rem $factor $rem nope\n";
		$time+=($input[$i-$nx]*$factor);
		$nx=1;
		last;
	    }
	    
	}
    }
    print "endloop: $time $factor\n";
}
