#!/usr/bin/perl
use Switch;
@lines = <>;
my $numlines=$.;
print "nlines: $numlines\n";
#print @lines;

my $repl=0;
my $done=0;

while(!$done)
{
    #her bytter vi en og en nop/jmp
    # $repl er den vi skal bytte
    # $replc er telleren i denne runden
    my $replc=0;
    my $noloop=1;
    my $pc=0;

    my $acc=0;
    my @hasbeen;
    while($noloop && ($pc < $numlines))
    {
	if ($hasbeen[$pc])
	{
#	    print "loop!\n"; 
	    $noloop=0;
	}
	$lines[$pc] =~ /(\w+)\s\+?(\-?\d+)/;
#	print "inner loop $pc: $1 $2 $replc $repl\n";
	$hasbeen[$pc]=1;
	switch($1) {
	    case "acc" { $acc += $2; }
	    case "jmp" { if($replc == $repl)
			 { 
#			     print "byttj $replc $repl\n";
			 }
			 else
			 {
#			     print "ikkebyttj $replc $repl\n";
			     $pc += ($2-1);
			 }
			 $replc++;
	    }
	    case "nop" { if($replc == $repl)
			 {
#			     print "byttn $replc $repl\n";
			     $pc += ($2-1);
			 }
			 else
			 {
#			     print "ikkebyttn $replc $repl\n";
			 }
			 $replc++;
	    }
	}
	    $pc++;
	    print "inner end $pc: $1 $2 $replc $repl acc: $acc\n";
    }

    print "outer loop:  $repl $acc\n\n";
if($pc==$numlines) {$done=1;}

$repl++;
}
