#!/usr/bin/perl

@in=<>;


sub isup
    #retur true om parameter er upcase
{
    my $tt=$_[0];
        return ($tt =~ /[[:upper:]]+/);
}

my %visits;
my $r;

sub rec
    # tar startpos som input, kjør rekursivt til vi kommer til end. 
{
    my $w=$_[0];
    print "w: $w\n";
    $visits{$w}++;
    if(isup($w) || ($visits{$w} < 2))
    {
	print "ok, $w $visits{$w}\n";
	   for my $l (@in)
	   {
	       $l =~ /(\w+)-(\w+)/;
	       $a=$1;
	       $b=$2;
	       
	       $aup=isup($a);
	       $bup=isup($b);
#	       print "w: $w a: $a $aup b:$b $bup\n";
	       if ($a eq $w)
		   
	       {
		   if($b eq "end")
		   {
		       print "..aend..\n";
		       %visits=();
		       return "end";
		   }
#		   print "$l ahar $w\n";
		   $r= $a . "," . rec($b);
	       }
	       if($b eq $w)
	       {
		   if($b eq "end")
		   {
		       print "..bend..\n";
		       %visits=();
		       return "end";
		   }
#		   print "$l bhar $w\n";
		   $r= $b . "," . rec($a);
		   
	       }
	   }
    print "r: $r\n";
    }
    else
    {
    print "ret: $r\n";
	return;
    }
}


rec("start");

